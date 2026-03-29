#panda ger tabbeler 
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def load_csv(file_path):
    
    data = pd.read_csv(file_path)

    y = data.iloc[:, 0]        # första kolumnen (label), vilken siffra det är (0-9)
    X = data.iloc[:, 1:]       # resten (pixlar)

    # Normalisera pixlarna till intervallet [0, 1], svart/vit bilder har värden 0-255
    X = X / 255.0

    return X.values, y.values

#skapa en matrix där varje rad är en bild och varje kolumn är en pixel,
#  och där värdet är 1 för den klass som bilden tillhör och 0 för alla andra klasser
def one_hot_encode(y, num_classes=10):
    m = len(y)
    y_onehot = np.zeros((m, num_classes))
    y_onehot[np.arange(m), y] = 1
    return y_onehot

def split_data(X, y):
    
    #dela upp data i tränings data, validerings data och test data
    X_train, X_temp, y_train, y_temp = train_test_split(
        X, y, test_size=0.30, random_state=50
    )

    X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp, test_size=2/3, random_state=50
    )

    return X_train, y_train, X_val, y_val, X_test, y_test


def load_and_prepare_data(file_path):

    X, y = load_csv(file_path)

    y = one_hot_encode(y, 10)

    X_train, y_train, X_val, y_val, X_test, y_test = split_data(X, y)

    return X_train, y_train, X_val, y_val, X_test, y_test

