import cv2
import numpy as np

img = cv2.imread(r"C:\Users\Bhoomika KM\Downloads\lab CV\images.jpg", 0)
f = np.fft.fftshift(np.fft.fft2(img))

r, c = img.shape
mask = np.zeros((r, c), np.uint8)
cv2.circle(mask, (c//2, r//2), 30, 1, -1)

low = np.abs(np.fft.ifft2(np.fft.ifftshift(f * mask)))
high = np.abs(np.fft.ifft2(np.fft.ifftshift(f * (1 - mask))))

cv2.imshow("Original", img)
cv2.imshow("Low Pass", np.uint8(np.clip(low, 0, 255)))
cv2.imshow("High Pass", np.uint8(np.clip(high, 0, 255)))
cv2.waitKey(0)
cv2.destroyAllWindows()