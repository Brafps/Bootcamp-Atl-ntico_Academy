
# Importação das bibliotecas
import cv2
# Leitura da imagem com a função imread()
img = cv2.imread('ponte.jpg')


cv2.imshow("Original", img)

flip_horizontal = img[:,::-1]#comando equivalente abaixo
#flip_horizontal = cv2.flip(img, 1)
cv2.imshow("Flip Horizontal", flip_horizontal)


flip_vertical = img[::-1,:] #comando equivalente abaixo
#flip_vertical = cv2.flip(img, 0)
cv2.imshow("Flip Vertical", flip_vertical)

#flip_hv = img[::-1,::-1] #comando equivalente abaixo
flip_hv = cv2.flip(img, -1)

cv2.imshow("Flip Horizontal e Vertical", flip_hv)


#Essa linha vai estar presente em todos os códigos, visto que em todos vamos salvar as imagens geradas.
# sa linha vai estar presente em todos os códigos, visto que em todos vamos salvar as imagens geradas.

cv2.waitKey(0) #espera pressionar qualquer tecla

# Salvar a imagem no disco com função imwrite()
cv2.imwrite("img_geradas/flip_horizontal.jpg", flip_horizontal)
cv2.imwrite("img_geradas/flip_vertical.jpg", flip_vertical)
cv2.imwrite("img_geradas/flip_hv.jpg", flip_hv)