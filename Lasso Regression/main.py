# from sklearn.linear_model import Lasso
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error
# from sklearn.metrics import r2_score
# import numpy as np
#
# # Simulate data
# np.random.seed(42)
# X = 2 * np.random.rand(100, 1)
# y = 4 + 3 * X + np.random.randn(100, 1)
#
# # Split data
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#
# # Fit Lasso regression model
# lasso_model = Lasso(alpha=1.0)  # Alpha is the regularization parameter
# lasso_model.fit(X_train, y_train)
# y_pred = lasso_model.predict(X_test)
#
# # Evaluate model
# mse = mean_squared_error(y_test, y_pred)
# r2_score = r2_score(y_test, y_pred)
# print("Mean Squared Error:", mse)
# print("R2 score:", r2_score)





import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

X,y = make_regression(n_samples=100, n_features=1, n_informative=1, n_targets=1,noise=20,random_state=13)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

# plt.scatter(X,y)
# plt.show()


reg = LinearRegression()
reg.fit(X_train,y_train)
print(reg.coef_)
print(reg.intercept_)

# alphas = [0, 1, 5, 10, 30]
# plt.figure(figsize=(12, 6))
# plt.scatter(X, y)
# for i in alphas:
#     L = Lasso(alpha=i)
#     L.fit(X_train, y_train)
#     plt.plot(X_test, L.predict(X_test), label='alpha={}'.format(i))
# plt.legend()
# plt.show()



m = 100
x1 = 5 * np.random.rand(m, 1) - 2
x2 = 0.7 * x1 ** 2 - 2 * x1 + 3 + np.random.randn(m, 1)
#
# plt.scatter(x1, x2)
# plt.show()


from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge

def get_preds_lasso(x1, x2, alpha):
    model = Pipeline([
        ('poly_feats', PolynomialFeatures(degree=16)),
        ('lasso', Lasso(alpha=alpha))
    ])
    model.fit(x1, x2)
    return model.predict(x1)

alphas = [0, 0.1, 1]
cs = ['r', 'g', 'b']

plt.figure(figsize=(10, 6))
plt.plot(x1, x2, 'b+', label='Datapoints')

for alpha, c in zip(alphas, cs):
    preds = get_preds_lasso(x1, x2, alpha)
    # Plot
    plt.plot(sorted(x1[:, 0]), preds[np.argsort(x1[:, 0])], c, label='Alpha: {}'.format(alpha))

plt.legend()
plt.show()





