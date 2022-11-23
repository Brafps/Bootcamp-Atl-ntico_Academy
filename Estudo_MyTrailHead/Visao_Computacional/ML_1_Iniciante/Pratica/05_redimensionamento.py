# Importação das bibliotecas
import cv2
# Leitura da imagem com a função imread()
img = cv2.imread('ponte.jpg')


cv2.imshow("Original", img)
largura = img.shape[1]
altura = img.shape[0]
proporcao = float(altura/largura)
largura_nova = 240 #em pixels
altura_nova = int(largura_nova*proporcao)
tamanho_novo = (largura_nova, altura_nova)
img_redimensionada = cv2.resize(img,
tamanho_novo, interpolation = cv2.INTER_AREA)
cv2.imshow('Resultado', img_redimensionada)


#Essa linha vai estar presente em todos os códigos, visto que em todos vamos salvar as imagens geradas.
cv2.waitKey(0) #espera pressionar qualquer tecla
# Salvar a imagem no disco com função imwrite()
cv2.imwrite("img_geradas\ redimensionamento.jpg", img_redimensionada)

