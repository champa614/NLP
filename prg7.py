from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")
results = model(r"C:\Users\Bhoomika KM\Downloads\lab CV\images.jpg")

img = results[0].plot()
cv2.imshow("YOLOv8 Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()