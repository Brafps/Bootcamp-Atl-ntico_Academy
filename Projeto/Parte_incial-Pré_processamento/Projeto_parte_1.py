

# importando as biblíoteca

import os
import random
import cv2
import matplotlib.pyplot as plt
import numpy as np

#Caminho onde estão localizados os arquivos de imagem
caminho_tb = 'DataSet\\all_nods_benignos'

caminho_tm = 'DataSet\\all_nods_malignos'

#Montando as listas com os nomes dos arquivos
for root, dirs, files in os.walk(caminho_tb):
    dataset_benigno = [file for file in files]

for root, dirs, files in os.walk(caminho_tm):
    dataset_maligno = [file for file in files]

dataset = sorted(dataset_benigno + dataset_maligno)


#Selecionando uma imagem qualquer
img_selecionada = random.choice(dataset)


#Definindo o caminho para uso da função cv2.read() e posterior mostra da imagem.
if img_selecionada in dataset_benigno:
    path = caminho_tb + "\\" + img_selecionada
    img = cv2.imread(path)
else:
    path = caminho_tm + "\\" + img_selecionada
    img = cv2.imread(path)

#Mostrando o local da imagem
print(path)

#Mostrando a imagem original
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", img)


#montando o histograma da imagem
h = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.figure()
plt.title(f"Histograma da imagem {img_selecionada}")
plt.xlabel("Intensidade")
plt.ylabel("Qtde de Pixels")
plt.plot(h)
plt.xlim([0, 256])
plt.show()


#Fazendo suavização pelo filtro gausiano e verificando a binarização da imagem
suave = cv2.GaussianBlur(img, (7, 7), 0) # aplica blur
(T, bin) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY)
(T, binI) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY_INV)
resultado = np.vstack([
    np.hstack([suave, bin]),
    np.hstack([binI, cv2.bitwise_and(img, img, mask = binI)])
    ])

cv2.imshow("Binarização da imagem", resultado)


cv2.waitKey(0)