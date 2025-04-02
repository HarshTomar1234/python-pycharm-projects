from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np


def huber_loss_sklearn(y_true, y_pred, delta):
    mse_loss = mean_squared_error(y_true, y_pred)
    mae_loss = mean_absolute_error(y_true, y_pred)

    # Calculate Huber loss
    condition = np.abs(y_true - y_pred) <= delta
    huber_loss = np.where(condition, 0.5 * (y_true - y_pred) ** 2, delta * np.abs(y_true - y_pred) - 0.5 * delta)

    return np.mean(huber_loss)


# Example usage:
y_true = np.array([1, 2, 3, 10])
y_pred = np.array([1.5, 2.5, 2.8, 9])
delta = 1.0

loss = huber_loss_sklearn(y_true, y_pred, delta)
print("Huber Loss (sklearn):", loss)

import numpy as np


def huber_loss(y_true, y_pred, delta):
    error = y_true - y_pred
    quadratic_loss = 0.5 * (error ** 2)
    linear_loss = delta * (np.abs(error) - 0.5 * delta)

    # Calculate Huber loss
    condition = np.abs(error) <= delta
    huber_loss = np.where(condition, quadratic_loss, linear_loss)

    return np.mean(huber_loss)


# Example usage:
y_true = np.array([1, 2, 3, 10])
y_pred = np.array([1.5, 2.5, 2.8, 9])
delta = 1.0

loss = huber_loss(y_true, y_pred, delta)
print("Huber Loss:", loss)
