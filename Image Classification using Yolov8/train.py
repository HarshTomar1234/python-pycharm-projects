from ultralytics import YOLO

model = YOLO('yolov8n-cls.pt')  # load a pretrained model (recommended for training)

model.train(data='C:/Users/Harsh/OneDrive/Documents/Desktop/Weather dataset'
            ,epochs=20, imgsz=64)