# Importação das bibliotecas

import numpy as np
import cv2

#Leitura
img = cv2.imread('ponte.jpg')

#Tomando os canais em tom cinza
(canalAzul, canalVerde, canalVermelho) = cv2.split(img)

#Definindo matriz de zeros
zeros = np.zeros(img.shape[:2], dtype = "uint8")
print("O tamanho da matriz de zeros é =", img.shape[:2])


CanalVermelhoOriginal = cv2.merge([zeros, zeros, canalVermelho])
CanalVerdeOriginal = cv2.merge([zeros, canalVerde, zeros])
CanalAzulOriginal = cv2.merge([canalAzul, zeros, zeros])


cv2.imshow("Vermelho", CanalVermelhoOriginal)
cv2.imshow("Verde", CanalVerdeOriginal)
cv2.imshow("Azul", CanalAzulOriginal)
cv2.imshow("Original", img)


#Também é possível alterar individualmente as Numpy Arrays que formam cada canal e depois juntá-las para criar novamente a imagem. Para isso use o comando:
#resultado = cv2.merge([canalAzul, canalVerde, canalVermelho])


#Essa linha vai estar presente em todos os códigos, visto que em todos vamos salvar as imagens geradas.
cv2.waitKey(0) #espera pressionar qualquer tecla
# Salvar a imagem no disco com função imwrite()
cv2.imwrite("img_geradas\CanalVermelhoOriginal.jpg", CanalVermelhoOriginal)

cv2.imwrite("img_geradas\CanalVerde.jpg", CanalVerdeOriginal)

cv2.imwrite("img_geradas\CanalAzulOriginal.jpg", CanalAzulOriginal)