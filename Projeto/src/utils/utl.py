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

def save_image(image,image_name):
    '''
    :param image: variável que contém a imagem
    :param image_name: nome para o arquivo da imagem
    :return: salvar um arquivo .PNG na pasta img_salvas
    '''
    path = "img_salvas\\"+f'{image_name}'+".PNG"
    cv2.imwrite(path, image)