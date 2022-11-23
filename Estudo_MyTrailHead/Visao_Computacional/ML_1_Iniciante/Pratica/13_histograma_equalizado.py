from matplotlib import pyplot as plt
import numpy as np
import cv2

img = cv2.imread('ponte.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
h_eq = cv2.equalizeHist(img)

plt.figure()
plt.title("Histograma Equalizado")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(h_eq.ravel(), 256, [0,256])
plt.xlim([0, 256])

plt.figure()
plt.title("Histograma Original")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.hist(img.ravel(), 256, [0,256])
plt.xlim([0, 256])

coluns = np.hstack([img, h_eq])
cv2.imshow("Img cinza e img equalizada", coluns)
cv2.imwrite("img_geradas\histograma_equalizado.jpg", coluns)
plt.show()


cv2.waitKey(0)