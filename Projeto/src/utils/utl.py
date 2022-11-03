import cv2
import matplotlib.pyplot as plt
import os
import random


def show_img(titulo, img, l = 6, a = 6):
    '''
    :param titulo: Escrever o título como string
    :param img: variável que contém a imagem
    :param a: largura desejada
    :param b: altura desejada
    :return: visualização da imagem desejada.
    '''
    try:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    except:
        pass
    plt.figure(figsize=(l, a))
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


def load_random_img():
    '''
    :return: retorna o par (nome da imagem, imagem) a imagem é aleatória.
    '''
    # Caminhos para os DataSets
    path_dataSet_benigno = "..\\..\\DataSet\\all_nods_benignos"
    path_dataSet_maligno = "..\\..\\DataSet\\all_nods_malignos"


    #Montando as listas com os nomes dos arquivos
    for root, dirs, files in os.walk(path_dataSet_benigno):
        dataset_benigno = [file for file in files]

    for root, dirs, files in os.walk(path_dataSet_maligno):
        dataset_maligno = [file for file in files]

    # lista com o nome de todos os arquivos
    dataset = sorted(dataset_benigno + dataset_maligno)

    #Selecionando uma imagem qualquer
    img_selecionada = random.choice(dataset)
    print(f"{img_selecionada} - Nome da imagem random gerada.")

    #Definindo o caminho para uso da função cv2.read() e posterior mostra da imagem.
    if img_selecionada in dataset_benigno:
        path = os.path.join(path_dataSet_benigno, img_selecionada)
        img = cv2.imread(path)
    else:
        path = os.path.join(path_dataSet_maligno, img_selecionada)
        img = cv2.imread(path)

    # Passando para cinza
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    return (f"{img_selecionada}", img_gray)


def load_img(name_img):
    '''
    :param name_img: Nome da imagem no dataset com extensão.
    :return: carrega a imagem desejada já em cinza.
    '''
    # Caminhos para os DataSets
    path_dataSet_benigno = "..\\..\\DataSet\\all_nods_benignos"
    path_dataSet_maligno = "..\\..\\DataSet\\all_nods_malignos"

    # Montando as listas com os nomes dos arquivos
    for root, dirs, files in os.walk(path_dataSet_benigno):
        dataset_benigno = [file for file in files]

    for root, dirs, files in os.walk(path_dataSet_maligno):
        dataset_maligno = [file for file in files]

    # lista com o nome de todos os arquivos
    dataset = sorted(dataset_benigno + dataset_maligno)

    # Selecionando uma imagem qualquer
    img_selecionada = name_img

    # Definindo o caminho para uso da função cv2.read() e posterior mostra da imagem.
    if img_selecionada in dataset_benigno:
        path = os.path.join(path_dataSet_benigno, img_selecionada)
        img = cv2.imread(path)
    else:
        path = os.path.join(path_dataSet_maligno, img_selecionada)
        img = cv2.imread(path)

    # Passando para cinza
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    return img_gray
