import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras import regularizers
from tensorflow.keras.models import load_model
import streamlit as st
import os

def train():
    
    os.system('mkdir -p model')

    model = Sequential()
    model.add(Dense(8, activation='relu', kernel_regularizer=regularizers.l2(0.001), input_shape = (1,)))
    model.add(Dense(8, activation='relu', kernel_regularizer=regularizers.l2(0.001)))
    model.add(Dense(1))

    model.compile(optimizer='adam',loss='mse')
    x = np.random.random((10000,1))*100-50
    y = x**2

    st.write('Training Model......')
    hist = model.fit(x,y,validation_split=0.2,
                epochs= 6000,
                batch_size=256)

    st.write('Model already trained!!!!')
    model.save("model/model.h5")       
    st.write('Model saved on: model/model.h5')    

def predict(sample):
    model = load_model('model/model.h5')
    return float(model.predict([sample])[0])