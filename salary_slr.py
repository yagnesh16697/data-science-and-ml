import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('salary.csv', sep=',', header=None, skiprows=1)

X = df.iloc[:, :-1].values
Y = df.iloc[:, -1].values

X = X.reshape(-1, 1)
model = LinearRegression()
model.fit(X, Y)

x_new = np.array([10]).reshape(-1, 1)

ans = model.predict(x_new)

print(ans)
