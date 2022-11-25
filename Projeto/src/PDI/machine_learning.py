
# Bibliotecas

import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from random import shuffle

import cv2
from skimage.measure import regionprops
from skimage.filters import threshold_otsu
from vc import cut_img
from pre_proc_good import pp_good

from sklearn import metrics,svm
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.preprocessing import MaxAbsScaler


# Preparando o dataset
def load_data(datadir, classes):
    training_data = []
    label = []
    for classe in range(len(classes)):
        path = os.path.join(datadir, classes[classe])
        shufled_list  = list(os.listdir(path))
        shuffle(shufled_list)
        for img in shufled_list:
            img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
            #print(img_array.shape)
            img_array = cut_img(img_array)
            #print(img_array.shape)
            unique = np.unique(img_array)
            if len(unique) == 1:
                continue
            training_data.append(img_array)
            label.append(classe)
    return training_data, label


# Extração dos Atributos
def get_contours_param(contour):
    contour_area = contour[0].filled_area
    contour_perimeter = contour[0].perimeter
    contour_convex_area = contour[0].convex_area
    diameter = contour[0].equivalent_diameter
    return contour_area , contour_perimeter, contour_convex_area, diameter


def features_extraction(images):
    features_list = []
    for image in images:
        thresh = threshold_otsu(image)
        binary = np.array(image > thresh).astype(int)
        white_pixel = np.where(binary > 0)
        if len(white_pixel[0]) > 7000:
            binary = abs(1-binary) # ajuste de imagens negativas
        regions = regionprops(binary)
        contour_area , contour_perimeter, contour_convex_area, diameter = get_contours_param(regions)
        features_list.append([contour_area , contour_perimeter, contour_convex_area, diameter])
    norm = MaxAbsScaler()
    norm.fit(features_list)
    norm_features = norm.transform(features_list)
    return norm_features

def features_extraction_ppg(images):
    features_list = []
    for image in images:
        binary = pp_good(image)
        regions = regionprops(binary)
        contour_area, contour_perimeter, contour_convex_area, diameter = get_contours_param(regions)
        features_list.append([contour_area, contour_perimeter, contour_convex_area, diameter])
    norm = MaxAbsScaler()
    norm.fit(features_list)
    norm_features = norm.transform(features_list)
    return norm_features





# Treinamento e Teste dos Classificadores
def generate_svm_model(train_data,label_train_data,test_data):
    clf = svm.SVC(kernel='linear')
    clf.fit(train_data, label_train_data)
    predicted = clf.predict(test_data)
    return predicted
def generate_SGDC_model(train_data,label_train_data,test_data):
    clf = SGDClassifier(loss="hinge", penalty="l2", max_iter=200)
    clf.fit(train_data, label_train_data)
    predicted = clf.predict(test_data)
    return predicted
def generate_naive_bayes_model(train_data,label_train_data,test_data):
    gnb = GaussianNB()
    gnb.fit(train_data, label_train_data)
    predicted = gnb.predict(test_data)
    return predicted
def generate_decision_tree_model(train_data,label_train_data,test_data):
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(train_data, label_train_data)
    predicted = clf.predict(test_data)
    return predicted
def generate_random_forest_model(X_train, y_train,test_data):
    rfc = RandomForestClassifier(criterion= 'entropy', max_depth= 8, max_features='auto', n_estimators=200)
    rfc.fit(X_train,y_train)
    predicted = rfc.predict(test_data)
    return predicted
def generate_MLP_model(X_train, y_train,test_data):
    classifier = MLPClassifier(hidden_layer_sizes=(100,100,100), max_iter=300,activation = 'relu',solver='adam',random_state=1)
    classifier.fit(X_train, y_train)
    predicted = classifier.predict(test_data)
    return predicted
def generate_knn_model(train_data,label_train_data,test_data):
    knn = KNeighborsClassifier()
    knn.fit(train_data,label_train_data)
    predicted = knn.predict(test_data)
    return predicted

# A função abaixo pega todos os classificadores
def gen_classifiers(train_data,label_train_data,test_data):
    return generate_knn_model(train_data,label_train_data,test_data),\
    generate_MLP_model(train_data,label_train_data,test_data),\
    generate_SGDC_model(train_data,label_train_data,test_data),\
    generate_svm_model(train_data,label_train_data,test_data),\
    generate_decision_tree_model(train_data,label_train_data,test_data),\
    generate_naive_bayes_model(train_data,label_train_data,test_data),\
    generate_random_forest_model(train_data,label_train_data,test_data),




