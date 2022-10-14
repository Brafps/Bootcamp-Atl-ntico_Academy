import numpy as np
import cv2
img = cv2.imread('ponte.jpg')
img = img[::2,::2] # Diminui a imagem
suave = np.vstack([
np.hstack([img,
cv2.medianBlur(img,  3)]),
np.hstack([cv2.medianBlur(img,  5),
cv2.medianBlur(img,  7)]),
np.hstack([cv2.medianBlur(img,  9),
cv2.medianBlur(img, 11)]),
])
cv2.imshow("Imagem original e suavizadas pela mediana", suave)
cv2.imwrite("img_geradas\suavizacao_medianaBlur.jpg", suave)
cv2.waitKey(0)