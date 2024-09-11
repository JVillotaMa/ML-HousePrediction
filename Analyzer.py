import numpy as np
import matplotlib.pyplot as plt

def stringToIntNumpy(array,ind,size):
    toRet=np.zeros([size])
    for i in range(size):
        toRet[i]=float(array[i][ind])
    return toRet

def scatter(neigh,in_X,in_Y):
    neighborhood=np.array(neigh)
    X=stringToIntNumpy(array=neighborhood,ind=in_X,size=neighborhood.shape[0])
    Y=stringToIntNumpy(array=neighborhood,ind=in_Y,size=neighborhood.shape[0])
    fig,ax = plt.subplots()
    ax.scatter(X,Y)
    plt.show()   

def plotter(X,Y,Y_pred):
    fig,ax = plt.subplots()
    ax.scatter(X,Y)
    ax.plot(X,Y_pred)
    plt.show()   


