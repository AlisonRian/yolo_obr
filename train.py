from ultralytics import YOLO

def train():
    # https://docs.ultralytics.com/models/yolov8
    model = YOLO("yolov8n.pt") # Carrega o modelo pré-treinado
    model.info()

    model.train(
        data="data.yaml", 
        epochs=100, 
        imgsz=640, 
        patience=30,
        device=0,
        batch=-1,
        amp=True
    )

if __name__ == "__main__":
    train()
    