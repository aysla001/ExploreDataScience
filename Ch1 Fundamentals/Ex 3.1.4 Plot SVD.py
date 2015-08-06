# Visualize the results of a clustering algorithm using the first two dimensions of the SVD. 
# The Data Science Officer prepared your editor with some code that has already fit the SVD, reduced your data, and fit a clustering model. Add code to plot the cluster results in the first two concept axis.  

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# load data from csv into numpy arrays
X = np.genfromtxt('mixed-spectra-matrix.csv', delimiter=';')

# mean center X
X = X - X.mean(1)[:, np.newaxis]

# calculate svd
U, s, Vh = np.linalg.svd(X)

# cluster
km = KMeans(n_clusters=4)
clusters = km.fit_predict(X)

# get the first 25 concepts
S25 = np.diag(s)[:, :25]
Vh25 = Vh[:25, :]
X25 = X.dot(Vh25.T)

# plot clusters on svd in 2d svd space
# use the first component as the x axis and the second as the y axis
plt.scatter(X25[:,0], X25[:,1], c=clusters)
plt.xlabel('Component 1')
plt.ylabel('Component 2')
plt.show()
