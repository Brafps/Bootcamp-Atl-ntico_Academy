# Importação das bibliotecas
import cv2
# Leitura da imagem com a função imread()
img = cv2.imread('ponte.jpg')


cv2.imshow("Original", img)

#Separando os canais
(CanalAzul, CanalVerde, CanalVermelho) = cv2.split(img)
#Lembrando que quanto mais ausente a cor, mais escuro fica.

cv2.imshow("Vermelho", CanalVermelho)
cv2.imshow("Verde", CanalVerde)
cv2.imshow("Azul", CanalAzul)
cv2.waitKey(0)


# Também é possível alterar individualmente as Numpy Arrays que formam cada canal e depois juntá-las para criar novamente a imagem. Para isso use o comando abaixo

resultado = cv2.merge([CanalAzul, CanalVerde, CanalVermelho])

cv2.imshow("Merge", resultado)



#Essa linha vai estar presente em todos os códigos, visto que em todos vamos salvar as imagens geradas.
cv2.waitKey(0) #espera pressionar qualquer tecla
# Salvar a imagem no disco com função imwrite()
cv2.imwrite("img_geradas\CanalVermelho.jpg", CanalVermelho)

cv2.imwrite("img_geradas\CanalVerde.jpg", CanalVerde)

cv2.imwrite("img_geradas\CanalAzul.jpg", CanalAzul)

cv2.imwrite("img_geradas\Merge.jpg", resultado)