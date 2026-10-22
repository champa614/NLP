import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Bhoomika KM\Downloads\lab CV\images.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)

lines = cv2.HoughLines(edges, 1, np.pi/180, 100)

if lines is not None:
    for line in lines:
        rho, theta = line[0]
        a, b = np.cos(theta), np.sin(theta)
        x, y = int(a*rho), int(b*rho)
        cv2.line(img, (x+1000*int(-b), y+1000*int(a)),
                 (x-1000*int(-b), y-1000*int(a)), (0,0,255), 2)

cv2.imshow("Hough Lines", img)
cv2.waitKey(0)
cv2.destroyAllWindows()