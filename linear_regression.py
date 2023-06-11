import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dataset
x = np.array([1000, 1300, 1500, 1700, 1750, 2000, 2100, 2300]
             ).reshape(-1, 1)  # Areas (in square feet)
# House prices (in thousands of dollars)
y = np.array([250, 320, 360, 400, 415, 490, 520, 570])

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(x, y)

# Get the slope (m) and y-intercept (b)
slope = model.coef_[0]
intercept = model.intercept_

# Predict using the model
x_new = np.array([1800]).reshape(-1, 1)  # New data point for prediction
y_new = model.predict(x_new)
print("Predicted price:", y_new[0])

# Plotting the regression line and data points
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, model.predict(x), color='red', label='Regression Line')
plt.scatter(x_new, y_new, color='green', label='New Prediction')
plt.xlabel('Area (sq. ft)')
plt.ylabel('Price (thousands of dollars)')
plt.title('Simple Linear Regression')
plt.legend()
plt.show()
