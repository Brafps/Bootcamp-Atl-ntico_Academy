
# Importação das bibliotecas
import cv2
# Leitura da imagem com a função imread()
imagem = cv2.imread('ponte.jpg')


#Leitura da posição linha
for y in range(0, imagem.shape[0]):
   #Leitura da posição coluna
    for x in range(0, imagem.shape[1]):
     #Modificação feita na coordenada
        imagem[y, x] = (255,0,0)

#Mostra a modificação
cv2.imshow("Imagem modificada para azul", imagem)



#Essa linha vai estar presente em todos os códigos, visto que em todos vamos salvar as imagens geradas.
cv2.waitKey(0) #espera pressionar qualquer tecla
# Salvar a imagem no disco com função imwrite()
cv2.imwrite("img_geradas\Imagem_modificada.jpg", imagem)