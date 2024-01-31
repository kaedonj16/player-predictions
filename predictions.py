#Package Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn.model_selection import train_test_split #train test split
from sklearn.linear_model import Ridge
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

def data(csv_file):
    df = pd.read_csv(csv_file)

    df_X = df.drop('PTS', axis = 1)
    df_Y = df['PTS']

    X_train, X_test, y_train, y_test = train_test_split(df_X, df_Y)

    rdg = Ridge(alpha = 0.01)
    rdg.fit(X_train, y_train)
    y_pred = rdg.predict(X_test)

    print(y_pred)

