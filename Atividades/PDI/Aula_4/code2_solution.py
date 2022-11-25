from tensorflow import keras
from tensorflow.keras.layers import Conv2D, MaxPooling2D,Flatten,Dense
from src.pdi_utils import load_sign_language_data


#carregando informações do dataset
data_train , label_train , data_val , label_val, _ , _  = load_sign_language_data()

#inicialização do modelo sequencial do keras
model = keras.Sequential()

#adição de uma cada convolucional 2D
model.add(Conv2D(4, kernel_size=(3, 3), activation= 'relu',input_shape=data_train.shape[1:],padding='same'))

#adição de uma camada de redução maxpooling
model.add(MaxPooling2D(pool_size=(2,2),padding='same'))

#transformação dos dados em 1 dimensão
model.add(Flatten(pool_size=(2,2),padding='same'))

#adição da camada densa (MLP)
model.add(Dense(29, pool_size=(2,2),activation= 'relu'))

#compilação do modelo
model.___(loss='___', optimizer='____',metrics=['sparse_categorical_accuracy'])

# treinamento do modelo
model.__(___, __, validation_data= (__, __), epochs=__)
