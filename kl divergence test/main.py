# from sklearn.metrics import mutual_info_score
# import numpy as np
#
# # Example true distribution
# p_distribution = np.array([0.2, 0.3, 0.5])
#
# # Example predicted distribution
# q_distribution = np.array([0.3, 0.4, 0.3])
#
# # Calculate KL Divergence using scikit-learn
# kl_divergence_sklearn = mutual_info_score(p_distribution, q_distribution)
# print(f'KL Divergence (sklearn): {kl_divergence_sklearn:.4f}')
#
#
#
# from scipy.stats import entropy
#
# # Calculate KL Divergence using scipy.stats.entropy
# kl_divergence_scipy = entropy(p_distribution, q_distribution)
# print(f'KL Divergence (scipy): {kl_divergence_scipy:.4f}')



# from sklearn.metrics import log_loss
# import numpy as np
#
# def focal_loss(y_true, y_pred, alpha=0.25, gamma=2.0):
#     epsilon = 1e-9
#     p = np.clip(y_pred, epsilon, 1 - epsilon)
#     alpha_t = np.where(y_true == 1, alpha, 1 - alpha)
#     focal_loss = - alpha_t * (1 - p)**gamma * np.log(p)
#     return np.mean(focal_loss, axis=-1)  # Sum across classes and take the mean
#
# # Custom loss function for scikit-learn
# def focal_loss_sklearn(y_true, y_pred):
#     return focal_loss(y_true, y_pred)




# # Example usage:
# y_true = np.array([[1, 0], [1, 0], [0, 1], [0, 1]])  # Example for a multi-class scenario
# y_pred = np.array([[0.9, 0.1], [0.7, 0.3], [0.2, 0.8], [0.6, 0.4]])
#
# loss = log_loss(y_true, y_pred, sample_weight=focal_loss_sklearn(y_true, y_pred))
# print("Focal Loss (sklearn):", loss)



#  DBSCAN Clustering
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np

# Generate synthetic data
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=1.0, random_state=42)

# DBSCAN
dbscan = DBSCAN(eps=0.8, min_samples=5)
labels = dbscan.fit_predict(X)

# Visualize the clusters
unique_labels = set(labels)
colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]

for k, col in zip(unique_labels, colors):
    if k == -1:
        col = [0, 0, 0, 1]  # Noise points in black

    class_member_mask = (labels == k)
    xy = X[class_member_mask]
    plt.scatter(xy[:, 0], xy[:, 1], color=tuple(col), s=50)

plt.title('DBSCAN Clustering')
plt.show()
















