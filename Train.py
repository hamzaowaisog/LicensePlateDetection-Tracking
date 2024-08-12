from ultralytics import YOLO

save_dir = r'.\checkpoints'

model = YOLO('yolov8n.pt')

if __name__ == "__main__" :
    model.info()
    results = model.train(data=r"E:\LicensePlateDetection-Tracking\License-Plate-Recognition-4\data.yaml", epochs=20 , imgsz=640, save=True,patience = 5, project=save_dir , name= 'checkpoints')

