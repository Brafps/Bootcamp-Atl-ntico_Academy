# Importação das bibliotecas
import cv2
# Leitura da imagem com a função imread()
img = cv2.imread('ponte.jpg')

(alt, lar) = img.shape[:2] #captura altura e largura
centro = (lar // 2, alt // 2) #acha o centro
M = cv2.getRotationMatrix2D(centro, 30, 1.0)#30 graus
img_rotacionada = cv2.warpAffine(img, M, (lar, alt))
cv2.imshow("Imagem rotacionada em 30 graus", img_rotacionada)

#Essa linha vai estar presente em todos os códigos, visto que em todos vamos salvar as imagens geradas.
cv2.waitKey(0) #espera pressionar qualquer tecla
# Salvar a imagem no disco com função imwrite()
cv2.imwrite("img_geradas\ Rotate.jpg", img_rotacionada)

