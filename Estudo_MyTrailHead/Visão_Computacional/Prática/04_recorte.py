# Importação das bibliotecas
import cv2
# Leitura da imagem com a função imread()
imagem = cv2.imread('ponte.jpg')

recorte = imagem[100:200, 100:200]
cv2.imshow("Recorte da imagem", recorte)


#Essa linha vai estar presente em todos os códigos, visto que em todos vamos salvar as imagens geradas.
cv2.waitKey(0) #espera pressionar qualquer tecla
# Salvar a imagem no disco com função imwrite()
cv2.imwrite("img_geradas\ recorte.jpg", recorte)

