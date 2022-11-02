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