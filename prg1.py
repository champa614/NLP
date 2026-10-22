import cv2
img = cv2.imread(r"C:\Users\Bhoomika KM\Downloads\lab CV\images.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cmyk = 255 - cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.imshow("Gray", gray)
cv2.imshow("HSV", hsv)
cv2.imshow("CMYK Approximation", cmyk)
cv2.waitKey(0)
cv2.destroyAllWindows()