import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# Dataset
x = np.array([1000, 1300, 1500, 1700, 1750, 2000, 2100, 2300]
             ).reshape(-1, 1)  # Areas (in square feet)
# House prices (in thousands of dollars)
y = np.array([250, 320, 360, 400, 415, 490, 520, 570])


model = LinearRegression()

model.fit(x, y)

slop = model.coef_[0]
intercept = model.intercept_

x_new = np.array([1888]).reshape(-1, 1)
x_new = np.array([1888]).reshape(-1, 1)
y_new = model.predict(x_new)


(print("Predicted price:", y_new[0]))
