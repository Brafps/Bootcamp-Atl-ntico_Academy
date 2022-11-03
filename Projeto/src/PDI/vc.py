import cv2
import numpy as np

def cut_img(imagem, l, a):
    '''
    :param imagem: variável que contém a imagem
    :param l: largura desejada para o recorte
    :param a: altura desejada para o recorte
    :return: recorte da imagem
    '''
    (largura, altura, canais) = np.shape(imagem)
    (c_x, c_y) = (largura//2, altura//2)
    return imagem[c_x - l: c_x + l, c_y - a: c_y + a]

