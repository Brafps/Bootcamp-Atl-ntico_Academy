
import cv2
from utils import show_image


def recorte(imagem, l, a):
    '''
    imagem: Caminho da imagem; l: largura desejada para o recorte; a: altura desejada para o recorte
    '''
    (largura, altura, canais) = imagem.shape
    (c_x, c_y) = (largura//2, altura//2)
    return imagem[c_x - l : c_x + l, c_y - a : c_y + a]

