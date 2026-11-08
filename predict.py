from ultralytics import YOLO

best_model_path = r"detect\train\weights\best.pt"
model = YOLO(best_model_path)
model.predict(
    source=r"data\test\images",
    conf=0.4,
    imgsz=640,
    retina_masks=True,
    save=True
    ) 