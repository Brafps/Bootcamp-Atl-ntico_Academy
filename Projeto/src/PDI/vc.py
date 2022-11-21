import cv2
import numpy as np
import skimage
from skimage import segmentation
from matplotlib import pyplot as plt

def cut_img(imagem, l = 50, a = 50):
    '''
    :param imagem: variável que contém a imagem.
    :param l: largura desejada para o recorte.
    :param a: altura desejada para o recorte.
    :return: recorte da imagem com seu centro no centro da imagem original.
    '''
    (c_x, c_y) = (100, 100)
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

def white_to_gray(img):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i, j] > 253:
                img[i, j] = 253
    return img

def define_pleural_nod(img, perc=0.3):
  count = 0

  img_binary = cv2.threshold(img.copy(), 70, 255, cv2.THRESH_BINARY)[1]

  for i in range(100):

    if img_binary[0][i] != 0: count += 1
    if img_binary[i][0] != 0: count += 1
    if img_binary[i][99] != 0: count += 1
    if img_binary[99][i] != 0: count += 1

  return count / (4 * 100) > perc


def remove_pleura(img, c_a = 50, c_b = 50):
  original_img = img
  # display_img(array_of_images_malignos[img_number])
  # 60 th
  original = cv2.threshold(original_img, 10, 255, cv2.THRESH_BINARY)[1]

  # display_img(original)

  new_color = 50
  contours, h = cv2.findContours(original.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  (x, y) = original.shape
  # print(contours)

  image = cv2.drawContours(original.copy(), contours, -1, (new_color, 0, 0), 1)
  # print('Contorno total')
  # display_img(image)

  initial_contour = image
  partial_complement = image.copy()

  for index in range(x):

    if image[0][index] != new_color: partial_complement[0][index] = new_color
    if image[x - 1][index] != new_color: partial_complement[x - 1][index] = new_color
    if image[index][0] != new_color: partial_complement[index][0] = new_color
    if image[index][y - 1] != new_color: partial_complement[index][y - 1] = new_color

  # print('contorno parcial')
  # display_img(partial_complement)

  complement = partial_complement.copy()

  for index in range(100):

    if image[0][index] == new_color and partial_complement[0][index] == new_color: complement[0][index] = original[0][
      index]
    if image[x - 1][index] == new_color and partial_complement[0][index] == new_color: complement[x - 1][index] = \
    original[x - 1][index]
    if image[index][0] == new_color and partial_complement[0][index] == new_color: complement[index][0] = \
    original[index][0]
    if image[index][y - 1] == new_color and partial_complement[0][index] == new_color: complement[index][y - 1] = \
    original[index][y - 1]

  # print('contorno complementar')
  # display_img(complement)

  contours, h = cv2.findContours(complement.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  # print(contours)

  # image = cv2.drawContours(complement.copy(),contours,-1,(255,0,0),1)
  # display_img(image)

  hull_list = []

  for i in range(len(contours)):
    hull = cv2.convexHull(contours[i])
    hull_list.append(hull)

  # drawing = np.zeros((complement.shape[0], complement.shape[1]), dtype=np.uint8)
  drawing = complement.copy()

  for i in range(len(contours)):
    # color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    # cv2.drawContours(drawing, contours, i, new_color)
    cv2.drawContours(drawing, hull_list, i, new_color, lineType=cv2.LINE_4, thickness=1)

  # print('convex hull')
  # display_img(drawing)

  # print(complement.shape,drawing.shape)
  final_result = cv2.bitwise_and(initial_contour, drawing)
  # display_img(final_result)

  new_value = 30

  # display_img(final_result)
  print(final_result.shape)
  flood_again = segmentation.flood_fill(final_result, (c_a, c_b), new_value=new_value, connectivity=1)
  # display_img(flood_again)

  nodule = original_img.copy()
  # display_img(nodule)

  for i, row in enumerate(flood_again):

    for j, pixel in enumerate(row):

      if pixel != new_value: nodule[i][j] = 0

  return nodule