import cv2
import os
import random
import cv2
import skimage
import matplotlib.pyplot as plt
import numpy as np
import tolerance as tolerance
from skimage import segmentation


from src.utils.utl import load_random_img, show_img, load_img, escrever
from vc import histograma, cut_img, white_to_gray, define_pleural_nod, remove_pleura

#(nome , imagem, tipo) = load_random_img()
#(nome , imagem, tipo) = load_img("06450")


#imagem = cut_img(imagem)
#original = imagem

def pp_good(img):
  img = white_to_gray(img)

  gray = img[50, 50]
  (c_1, c_2) = (50, 50)
  for i in range(9):
    # Horizontal vertical
    if img[46 + i, 50] > img[50, 46 + i]:
      if img[46 + i, 50] > gray:
        (c_1, c_2) = (46 + i, 50)
        gray = img[46 + i, 50]
    else:
      if img[50, 46 + i] > gray:
        (c_1, c_2) = (50, 46 + i)
        gray = img[50, 46 + i]

  if gray < 90:
    tol = 30
  else:
    tol = 90

  #print(gray)
  #print((c_1, c_2))



  img = cv2.GaussianBlur(img, (3,3), 0)
  #show_img("Img_Gau", img)
  img = segmentation.flood_fill(img, (c_1, c_2), 255, tolerance = tol)
  #show_img("Img_seg", img)
  img_pp = cv2.threshold(img, 254, 255, cv2.THRESH_TOZERO)[1]
  #show_img("Img_tre", img)


  # Passando a mascara
  #img_pp = cv2.bitwise_and(original, original, mask = img_pp)


  if define_pleural_nod(img_pp):
    img_pp = remove_pleura(img_pp, c_1, c_2)
  return img_pp


'''
img_pp = pp_good(imagem)

escrever(img_pp, "Segmentada")
escrever(original, "Original")

image = np.hstack([original, img_pp])

show_img(f"Tumor {nome}, {tipo}", image)
'''
