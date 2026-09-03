import json
import math
import time
from pathlib import Path

import cv2
from ultralytics import YOLO

# -----------------------------
# SETTINGS
# -----------------------------
CAMERA_INDEX = 1
MODEL_NAME = "yolo11n.pt"   # use working default model first

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

LIVE_SCAN_FILE = DATA_DIR / "live_scan.json"
LIVE_OBJECTS_FILE = DATA_DIR / "live_objects.json"
SNAPSHOT_FILE = DATA_DIR / "latest_snapshot.json"
FRAME_FILE = DATA_DIR / "latest_frame.jpg"

COMMON_CLASSES = {"person", "chair", "laptop", "bottle"}


def safe_load_json(file_path, default):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default


def safe_write_json(file_path, data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def update_snapshot(objects):
    scan_points = safe_load_json(LIVE_SCAN_FILE, [])
    snapshot = {
        "scan_points": scan_points,
        "objects": objects
    }
    safe_write_json(SNAPSHOT_FILE, snapshot)


def polar_to_cartesian(angle_deg, distance_cm):
    angle_rad = math.radians(angle_deg)
    x = round(distance_cm * math.cos(angle_rad), 2)
    y = round(distance_cm * math.sin(angle_rad), 2)
    return x, y


def get_image_position(center_x, frame_width):
    if center_x < frame_width / 3:
        return "left"
    elif center_x < 2 * frame_width / 3:
        return "center"
    return "right"


def pick_scan_for_position(scan_points, image_position):
    if not scan_points:
        return None

    if image_position == "left":
        candidates = [p for p in scan_points if 120 <= p["angle_deg"] <= 180]
        target_angle = 150
    elif image_position == "center":
        candidates = [p for p in scan_points if 60 <= p["angle_deg"] <= 120]
        target_angle = 90
    else:
        candidates = [p for p in scan_points if 0 <= p["angle_deg"] <= 60]
        target_angle = 30

    if not candidates:
        return None

    return min(candidates, key=lambda p: abs(p["angle_deg"] - target_angle))


def main():
    print("[INFO] Loading YOLO model...")
    model = YOLO(MODEL_NAME)

    cap = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_DSHOW)
    time.sleep(2)

    if not cap.isOpened():
        raise RuntimeError(f"Could not open camera index {CAMERA_INDEX}")

    print("[INFO] Object fusion collector started. Press Q to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[WARN] Failed to read frame.")
            break

        scan_points = safe_load_json(LIVE_SCAN_FILE, [])

        results = model.predict(
            source=frame,
            conf=0.35,
            imgsz=416,
            verbose=False
        )

        result = results[0]
        fused_objects = []
        display_frame = frame.copy()

        if result.boxes is not None and len(result.boxes) > 0:
            frame_width = frame.shape[1]

            for box in result.boxes:
                cls_id = int(box.cls[0].item())
                conf = float(box.conf[0].item())
                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())

                label = model.names[cls_id]
                if label not in COMMON_CLASSES:
                    continue

                center_x = (x1 + x2) // 2
                image_position = get_image_position(center_x, frame_width)

                matched_scan = pick_scan_for_position(scan_points, image_position)
                if matched_scan is None:
                    continue

                angle_deg = matched_scan["angle_deg"]
                distance_cm = matched_scan["distance_cm"]
                x, y = polar_to_cartesian(angle_deg, distance_cm)

                fused_obj = {
                    "timestamp": round(time.time(), 3),
                    "label": label,
                    "confidence": round(conf, 3),
                    "angle_deg": angle_deg,
                    "distance_cm": distance_cm,
                    "x": x,
                    "y": y,
                    "bbox": [x1, y1, x2, y2],
                    "image_position": image_position
                }
                fused_objects.append(fused_obj)

                cv2.rectangle(display_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(
                    display_frame,
                    f"{label} {conf:.2f}",
                    (x1, max(30, y1 - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2
                )

        safe_write_json(LIVE_OBJECTS_FILE, fused_objects)
        update_snapshot(fused_objects)
        cv2.imwrite(str(FRAME_FILE), display_frame)

        cv2.imshow("Object Fusion Collector", display_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("[INFO] Object fusion collector stopped.")


if __name__ == "__main__":
    main()