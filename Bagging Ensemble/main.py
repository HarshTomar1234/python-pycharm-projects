# Bagging Clasifier

from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Create a synthetic dataset
X, y = make_classification(n_samples=1000, n_features=20, random_state=42)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a base classifier (e.g., Decision Tree)
base_classifier = DecisionTreeClassifier(random_state=42)

# Create a BaggingClassifier
bagging_classifier = BaggingClassifier(
    base_classifier,
    n_estimators=10,  # Number of base models
    max_samples=0.8,  # Size of each bootstrap sample
    bootstrap=True,
    random_state=42
)

# Train the ensemble model
bagging_classifier.fit(X_train, y_train)

# Make predictions
y_pred = bagging_classifier.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


# Bagging Regressor

from sklearn.ensemble import BaggingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Create a synthetic regression dataset
X, y = make_regression(n_samples=1000, n_features=20, noise=0.1, random_state=42)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create individual regressors
regressor1 = LinearRegression()
regressor2 = DecisionTreeRegressor(random_state=42)
regressor3 = SVR()

# Create a BaggingRegressor
bagging_regressor = BaggingRegressor(
    estimator=None,  # Specify your base estimator
    n_estimators=10,       # Number of base models
    max_samples=0.8,       # Size of each bootstrap sample (as a proportion)
    bootstrap=True,
    random_state=42
)

# Train the ensemble model
bagging_regressor.fit(X_train, y_train)

# Make predictions
y_pred = bagging_regressor.predict(X_test)

# Evaluate mean squared error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
