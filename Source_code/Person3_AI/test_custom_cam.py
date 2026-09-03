import cv2
import time
from ultralytics import YOLO

# Load your trained custom model
model = YOLO(r"runs\detect\train\weights\best.pt")

# Camera index = 1
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
time.sleep(2)

if not cap.isOpened():
    raise RuntimeError("Could not open camera index 1")

print("Custom YOLO detection started")
print("Press Q to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to read frame")
        break

    results = model.predict(
        source=frame,
        conf=0.15,
        imgsz=416,
        verbose=False
    )
    result = results[0]

    annotated_frame = result.plot()

    if result.boxes is not None and len(result.boxes) > 0:
        print("\nDetected objects:")
        for box in result.boxes:
            cls_id = int(box.cls[0].item())
            conf = float(box.conf[0].item())
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())

            label = model.names[cls_id]

            print({
                "class": label,
                "confidence": round(conf, 3),
                "bbox": [x1, y1, x2, y2]
            })

    cv2.imshow("Custom YOLO Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()