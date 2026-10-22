import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Bhoomika KM\Downloads\lab CV\images.jpg", 0)
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
k = np.ones((3, 3), np.uint8)

cv2.imshow("Dilation", cv2.dilate(binary, k))
cv2.imshow("Erosion", cv2.erode(binary, k))
cv2.imshow("Opening", cv2.morphologyEx(binary, cv2.MORPH_OPEN, k))
cv2.imshow("Closing", cv2.morphologyEx(binary, cv2.MORPH_CLOSE, k))

cv2.waitKey(0)
cv2.destroyAllWindows()