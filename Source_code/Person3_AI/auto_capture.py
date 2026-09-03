import cv2
import os
import time

# ===== SETTINGS =====
CAMERA_INDEX = 1
SAVE_FOLDER = "raw_images"
CAPTURE_INTERVAL = 0.6  # seconds between photos
TOTAL_IMAGES = 100       # how many images to capture
# ====================

def main():
    class_name = input("Enter class name (person/chair/laptop/wire/fan/window/water_bottle): ").strip().lower()

    if class_name == "":
        print("Class name cannot be empty.")
        return

    os.makedirs(SAVE_FOLDER, exist_ok=True)

    cap = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_DSHOW)
    time.sleep(2)

    if not cap.isOpened():
        print("Could not open camera index 1")
        return

    print(f"\nCamera opened.")
    print(f"Class: {class_name}")
    print(f"Will capture {TOTAL_IMAGES} images")
    print("Press S to start capture")
    print("Press Q to quit\n")

    started = False
    count = 0
    last_capture_time = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to read frame")
            break

        display_frame = frame.copy()

        cv2.putText(display_frame, f"Class: {class_name}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.putText(display_frame, f"Captured: {count}/{TOTAL_IMAGES}", (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

        if not started:
            cv2.putText(display_frame, "Press S to start", (20, 130),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        else:
            cv2.putText(display_frame, "Auto capturing...", (20, 130),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("Auto Capture - Camera 1", display_frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("s") and not started:
            started = True
            last_capture_time = time.time()
            print("Capture started...")

        if key == ord("q"):
            print("Quit.")
            break

        if started and count < TOTAL_IMAGES:
            current_time = time.time()
            if current_time - last_capture_time >= CAPTURE_INTERVAL:
                filename = f"{class_name}_{count+1:03d}.jpg"
                filepath = os.path.join(SAVE_FOLDER, filename)
                cv2.imwrite(filepath, frame)
                count += 1
                last_capture_time = current_time
                print(f"Saved: {filepath}")

        if count >= TOTAL_IMAGES:
            print("\nFinished capturing images.")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
