
import cv2
import os
import random
import cv2
import matplotlib.pyplot as plt
import numpy as np

from src.utils.utl import show_img
from src.PDI.vc import recorte


recorte()

show_img("recorte", img)







'''
# Caminho onde esta localizado o datdaset
caminho_tb = 'DataSet\\all_nods_benignos'

caminho_tm = 'DataSet\\all_nods_malignos'

# Montando as listas com os nomes dos arquivos
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
'''