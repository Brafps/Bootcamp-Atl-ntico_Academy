# Importação das bibliotecas
import cv2
# Leitura da imagem com a função imread()
img = cv2.imread('ponte.jpg')


#print(img[40, 50])


(ca, cvd, cvm) = cv2.split(img)

print("imagem com ", img.shape[0], "linhas e", img.shape[1], "colunas", "canais", img.shape[2])

print(ca[40, 50])
print(cvd[40, 50])
print(cvm[40, 50])


#for i in range(0, img.shape[0]):
    #for j in range(0, img.shape[1]):
        #img[i, j] = (50)


#cv2.imshow("entendendo as cores", img)



#Essa linha vai estar presente em todos os códigos, visto que em todos vamos salvar as imagens geradas.
cv2.waitKey(0) #espera pressionar qualquer tecla
# Salvar a imagem no disco com função imwrite()
#cv2.imwrite("img_geradas\gray.jpg", gray)
