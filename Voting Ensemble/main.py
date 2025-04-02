# Voting Classifier

from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Create a synthetic dataset
X, y = make_classification(n_samples=1000, n_features=20, random_state=42)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create individual classifiers
classifier1 = LogisticRegression(random_state=42)
classifier2 = DecisionTreeClassifier(random_state=42)
classifier3 = SVC(probability=True, random_state=42)

# Create a VotingClassifier
voting_classifier = VotingClassifier(
    estimators=[('lr', classifier1), ('dt', classifier2), ('svm', classifier3)],
    voting='hard'  # Use 'soft' for soft voting
)

# Train the ensemble model
voting_classifier.fit(X_train, y_train)

# Make predictions
y_pred = voting_classifier.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


# Voting Regressor

from sklearn.ensemble import VotingRegressor
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

# Create a VotingRegressor
voting_regressor = VotingRegressor(
    estimators=[('lr', regressor1), ('dt', regressor2), ('svm', regressor3)]
)

# Train the ensemble model
voting_regressor.fit(X_train, y_train)

# Make predictions
y_pred = voting_regressor.predict(X_test)

# Evaluate mean squared error
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
