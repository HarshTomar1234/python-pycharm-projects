# Hard Margin SVM

from sklearn import datasets
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

# # Generate linearly separable data
# X, y = datasets.make_classification(n_samples=100, n_features=2, n_classes=2, n_informative=2, n_redundant=0, random_state=1)
#
# # Fit a Hard Margin SVM with C=1.0
# clf = SVC(kernel='linear', C=1.0)
# clf.fit(X, y)
#
# # Plot the decision boundary
# plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
# ax = plt.gca()
# xlim = ax.get_xlim()
# ylim = ax.get_ylim()
#
# # Create grid to evaluate model
# xx, yy = np.meshgrid(np.linspace(xlim[0], xlim[1], 50), np.linspace(ylim[0], ylim[1], 50))
# Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
#
# # Plot decision boundary and margins
# Z = Z.reshape(xx.shape)
# plt.contour(xx, yy, Z, colors='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])
# plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=100, facecolors='none', edgecolors='k')
# plt.title('Hard Margin SVM')
# plt.show()



# Soft Margin SVM

from sklearn import datasets
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

# Generate non-linearly separable data
X, y = datasets.make_classification(n_samples=100, n_features=2, n_classes=2, n_informative=2, n_redundant=0, random_state=1)

# Fit a Soft Margin SVM with C=1.0
clf = SVC(kernel='linear', C=1.0)
clf.fit(X, y)

# Plot the decision boundary
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# Create grid to evaluate model
xx, yy = np.meshgrid(np.linspace(xlim[0], xlim[1], 50), np.linspace(ylim[0], ylim[1], 50))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])

# Plot decision boundary and margins
Z = Z.reshape(xx.shape)
plt.contour(xx, yy, Z, colors='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])
plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=100, facecolors='none', edgecolors='k')
plt.title('Soft Margin SVM')
plt.show()
