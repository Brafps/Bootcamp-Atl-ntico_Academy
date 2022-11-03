import cv2
import numpy as np
from matplotlib import pyplot as plt

def cut_img(imagem, l = 50, a = 50):
    '''
    :param imagem: variável que contém a imagem.
    :param l: largura desejada para o recorte.
    :param a: altura desejada para o recorte.
    :return: recorte da imagem com seu centro no centro da imagem original.
    '''
    (largura, altura) = (imagem.shape[0], imagem.shape[1])
    (c_x, c_y) = (largura//2, altura//2)
    return imagem[c_x - l: c_x + l, c_y - a: c_y + a]


def histograma(name, img):
    '''
    :param name: nome da imagem
    :param img: variável que contém a imagem P&B
    :return: retorna o histograma da imagem.
    '''
    #Função calcHist para calcular o histograma da imagem
    h = cv2.calcHist([img], [0], None, [256], [0, 256])
    plt.figure()
    plt.title(f"{name}")
    plt.xlabel("Intensidade")
    plt.ylabel("Qtde de Pixels")
    plt.plot(h)
    plt.xlim([0, 256])
    plt.show()
    cv2.waitKey(0)