import cv2
import torch
from torchvision.models.detection import fasterrcnn_resnet50_fpn, FasterRCNN_ResNet50_FPN_Weights

weights = FasterRCNN_ResNet50_FPN_Weights.DEFAULT
model = fasterrcnn_resnet50_fpn(weights=weights).eval()

img = cv2.imread(r"C:\Users\Bhoomika KM\Downloads\lab CV\images.jpg")
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
x = torch.from_numpy(rgb).permute(2, 0, 1).float() / 255

with torch.no_grad():
    out = model([x])[0]

for box, score in zip(out["boxes"], out["scores"]):
    if score > 0.7:
        x1, y1, x2, y2 = map(int, box)
        cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)

cv2.imshow("Faster R-CNN", img)
cv2.waitKey(0)
cv2.destroyAllWindows()