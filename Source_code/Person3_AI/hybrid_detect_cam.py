import cv2
import time
from ultralytics import YOLO

# Default model for common objects
default_model = YOLO("yolo11n.pt")

# Custom model for your trained classes
custom_model = YOLO("best.pt")

# Common classes from default YOLO
COMMON_CLASSES = {"person", "chair", "laptop", "bottle"}

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
time.sleep(2)

if not cap.isOpened():
    raise RuntimeError("Could not open camera index 1")

print("Hybrid detection started")
print("Press Q to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to read frame")
        break

    display_frame = frame.copy()

    # ---------- Default YOLO ----------
    default_results = default_model.predict(
        source=frame,
        conf=0.35,
        imgsz=416,
        verbose=False
    )
    d_result = default_results[0]

    if d_result.boxes is not None and len(d_result.boxes) > 0:
        for box in d_result.boxes:
            cls_id = int(box.cls[0].item())
            conf = float(box.conf[0].item())
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            label = default_model.names[cls_id]

            if label in COMMON_CLASSES:
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

    # ---------- Custom YOLO ----------
    custom_results = custom_model.predict(
        source=frame,
        conf=0.15,
        imgsz=416,
        verbose=False
    )
    c_result = custom_results[0]

    if c_result.boxes is not None and len(c_result.boxes) > 0:
        for box in c_result.boxes:
            cls_id = int(box.cls[0].item())
            conf = float(box.conf[0].item())
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            label = custom_model.names[cls_id]

            if label in ["wire", "fan", "window"]:
                cv2.rectangle(display_frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                cv2.putText(
                    display_frame,
                    f"{label} {conf:.2f}",
                    (x1, max(30, y1 - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (255, 0, 0),
                    2
                )

    cv2.imshow("Hybrid Detection Camera 1", display_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()