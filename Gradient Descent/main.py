# Gradient Descent

import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Add a bias term to X
X_b = np.c_[np.ones((100, 1)), X]

# Initialize parameters
theta = np.random.randn(2, 1)

# Learning rate and number of epochs
alpha = 0.01
epochs = 100

# Batch Gradient Descent
def batch_gradient_descent(X, y, theta, alpha, epochs):
    m = len(y)
    for epoch in range(epochs):
        gradient = (1/m) * X.T.dot(X.dot(theta) - y)
        theta = theta - alpha * gradient
    return theta

# Apply Batch Gradient Descent
theta_batch = batch_gradient_descent(X_b, y, theta, alpha, epochs)

# Stochastic Gradient Descent
def stochastic_gradient_descent(X, y, theta, alpha, epochs):
    m = len(y)
    for epoch in range(epochs):
        for i in range(m):
            random_index = np.random.randint(m)
            xi = X[random_index:random_index + 1]
            yi = y[random_index:random_index + 1]
            gradient = xi.T.dot(xi.dot(theta) - yi)
            theta = theta - alpha * gradient
    return theta

# Apply Stochastic Gradient Descent
theta_stochastic = stochastic_gradient_descent(X_b, y, theta, alpha, epochs)

# Mini-Batch Gradient Descent
def mini_batch_gradient_descent(X, y, theta, alpha, epochs, batch_size):
    m = len(y)
    for epoch in range(epochs):
        for i in range(0, m, batch_size):
            xi = X[i:i + batch_size]
            yi = y[i:i + batch_size]
            gradient = (1/batch_size) * xi.T.dot(xi.dot(theta) - yi)
            theta = theta - alpha * gradient
    return theta

# Apply Mini-Batch Gradient Descent
batch_size = 20
theta_mini_batch = mini_batch_gradient_descent(X_b, y, theta, alpha, epochs, batch_size)

# Plot the results
plt.scatter(X, y, alpha=0.7, label='Original Data')
plt.plot(X, X_b.dot(theta_batch), label='Batch GD', color='red', linewidth=2)
plt.plot(X, X_b.dot(theta_stochastic), label='Stochastic GD', color='green', linewidth=2)
plt.plot(X, X_b.dot(theta_mini_batch), label='Mini-Batch GD', color='blue', linewidth=2)
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
