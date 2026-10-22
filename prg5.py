import cv2

img = cv2.imread(r"C:\Users\Bhoomika KM\Downloads\lab CV\images.jpg", 0)
lap = cv2.Laplacian(img, cv2.CV_64F)
edge = cv2.convertScaleAbs(lap)

cv2.imshow("Original", img)
cv2.imshow("Laplace Edge", edge)
cv2.waitKey(0)
cv2.destroyAllWindows()