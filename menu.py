from DataManager import differentNeigh 
from ModelCreation import suitingData,actModel
from DataManager import openCSV


import numpy as np
def menu():
    print("HELLO WELCOME TO YOURIMOP \n ENTER YOUR DATA")
    sf = float(input("Square Foot: "))
    nb = float(input("Number of bathrooms"))
    nf = float(input("Number of floors"))
    ren = float(input("Need a renovable? (0-1)"))
    new = float(input("New building? (0-1)"))

    neighboor = differentNeigh('data/generated_output.csv')
    for i in range(len(neighboor)):
        print(i+1,neighboor[i])
    s_neigh = input("Select neighborhood (1-20)")
    toRet = np.array([[sf,nb,nf,ren,new]])
    return neighboor[int(s_neigh)], toRet


def act():
    s,x_p = menu()
    neighborhood=openCSV('data/generated_output.csv')
    X,Y=suitingData(neighborhood.get(s),[2,5,6,8,9],7)
    model = actModel(X,Y)
    prediction=model.predict(x_p)
    print("Your house prediction is: ", prediction)

