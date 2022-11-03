import cv2
import os
import random
import cv2
import matplotlib.pyplot as plt
import numpy as np

from src.utils.utl import load_random_img, show_img, 
from vc import histograma, cut_img

(nome, img) = load_random_img()

img = cut_img(img)


show_img(nome, img)


histograma(nome, img)

