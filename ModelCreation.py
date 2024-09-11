import numpy as np
import tensorflow as tf
from keras import layers
from keras import Sequential
from sklearn.preprocessing import StandardScaler
from DataManager import openCSV
from Analyzer import  plotter

def suitingData(full,X_ind,Y_ind):
    """
    Inputs: full: array (n,m) all the data of one neighborhood
            X_ind: list with all the indicies that we want to put into the model
            Y_ind: The predicion i
    Output:
        X_train: freatures to train the model
        Y_train: price of the houses
    """
    m=len(full)
    n=len(X_ind)

    X_train = np.zeros([m,n])
    Y_train = np.zeros([m])
    for i in range(m):
        for j in range(n):
            X_train[i][j]=full[i][X_ind[j]]
            
        Y_train[i]=full[i][Y_ind]
    return X_train , Y_train 


def actModel(X_train,Y_train):

    

    model = Sequential(
        [ 
            layers.Dense(1080, activation = 'relu'),
            layers.Dense(720, activation = 'relu'),
            layers.Dense(360, activation = 'relu'),
            layers.Dense(180, activation = 'relu'),
            layers.Dense(60, activation = 'relu'),
            layers.Dense(80, activation = 'relu'),
            layers.Dense(48, activation = 'relu'),
            layers.Dense(24, activation = 'relu'),
            layers.Dense(1, activation = 'linear')   
        ]
    )
    model.compile(
        loss=tf.keras.losses.MeanAbsolutePercentageError(), 
    )
    
    model.fit(
        X_train,Y_train,
        epochs=100
    )
    
    return model


