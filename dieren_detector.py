from ultralytics import YOLO

#Load model
model = YOLO("yolov8n.pt")

#Use model
results = model.train(data='dieren.yaml', epochs=10)

#Validation
results = model.val()
