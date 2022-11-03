import cv2
import matplotlib.pyplot as plt


def show_img(titulo, img, a = 6.4, b = 4.8):
    try:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    except:
        pass
    plt.figure(figsize=(a, b))
    plt.title(titulo)
    plt.imshow(img, cmap='gray')
    plt.show()

def save_img(img,img_name):
    '''
    :param img: variável que contém a imagem
    :param img_name: nome para o arquivo da imagem
    :return: salvar um arquivo .PNG na pasta img_salvas
    '''
    path = "img_salvas\\"+f'{img_name}'+".PNG"
    cv2.imwrite(path, img)


def escrever(img, texto, cor=(255,0,0)):
    '''
    :param img: variável que contém a imagem
    :param texto: texto a ser colocado na imagem
    :param cor: deve-se colocar a cor do texto, por padrão é (255, 0, 0)
    :return: coloca um texto na imagem escolhida
    '''
    fonte = cv2.FONT_HERSHEY_SIMPLEX 
    cv2.putText(img, texto, (10,20), fonte, 0.5, cor, 0, cv2.LINE_AA)
