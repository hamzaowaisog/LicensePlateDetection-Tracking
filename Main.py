from ultralytics import YOLO
import cv2

coco_model = YOLO('yolov8n.pt')
license_plate_detector = YOLO('Model\LicensePlateDetection.pt')

cap = cv2.VideoCapture('Video\Input.mp4')

vehicles = [2,3,5,7]

frame_nmr = -1
ret = True
while ret:
  frame_nmr += 1
  ret, frame = cap.read()

  if ret and frame_nmr<10:
    #detect vehicles
    detections = coco_model(frame)[0]
    detections_= []
    for detection in detections.boxes.data.tolist():
      x1,y1,x2,y2,score,class_id = detection
      if int(class_id) in vehicles:
        detections_.append([x1,y1,x2,y2,score])

    #track vehicles


