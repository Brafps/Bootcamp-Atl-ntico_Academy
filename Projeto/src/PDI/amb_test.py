
import numpy as np
import pandas as pd

from src.utils.utl import show_img
from machine_learning import load_data, features_extraction, features_extraction_ppg, gen_classifiers
from sklearn.model_selection import train_test_split
from sklearn import metrics,svm
from sklearn.metrics import classification_report

# Logo, label = 0 benigno, label = 1 maligno
data, label = load_data('..\\..\\DataSet', ['all_nods_benignos','all_nods_malignos'])

for i in data:
    if i.shape[0] < 100:
        print(f"{i.shape[0]}")
    if i.shape[1] < 100:
        print(f"{i.shape[1]}")