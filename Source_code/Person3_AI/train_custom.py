from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("yolo11n.pt")

    model.train(
        data=r"C:\Users\Admin\OneDrive\Desktop\Hackathon_Custom_YOLO\roboflow_dataset\data.yaml",
        epochs=50,
        imgsz=640,
        batch=8
    )