
import numpy as np
import pandas as pd

from src.utils.utl import show_img
from machine_learning import load_data, features_extraction, features_extraction_ppg, gen_classifiers
from sklearn.model_selection import train_test_split
from sklearn import metrics,svm
from sklearn.metrics import classification_report

# Logo, label = 0 benigno, label = 1 maligno
data, label = load_data('..\\..\\DataSet', ['all_nods_benignos','all_nods_malignos'])



# Extraindo atributos
features = features_extraction(data)



# Separando para teste
X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.3)

results = gen_classifiers(X_train, y_train, X_test)


# Visualização da precisão dos classificadores

Classificadores = ["kNN", "MLP", "SGDC", "SVM", "DT", "NB", "RF"]

Resultados_acc = []
for i in range(len(Classificadores)):
    acc = metrics.accuracy_score(y_test, results[i])
    Resultados_acc.append(acc)
resultados_acc = np.array(Resultados_acc)

df = pd.DataFrame([resultados_acc], columns=[Classificadores], index=["accuracy"])

print(df)
