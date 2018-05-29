import sys
import os
import pandas as pd 
import numpy as np

def main():
    df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)
    return df

if __name__ == "__main__":
    df = main()
    y = df.iloc[0:100, 4].values
    print(y)
    y = np.where(y == 'Iris-setosa', -1, 1)
    print(y)