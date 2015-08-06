#Task 1
# The Data Science Officer prepared your editor with some code. Add code to instantiate and fit the PCA model. Then, tell matplotlib what arrays should be in the scatter plot to display explained variance plotted against number of components. If necessary, check the documentation for assistance. Make sure you keep all components.  


import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# load data from csv into numpy arrays
X = np.genfromtxt('mixed-spectra-matrix.csv', delimiter=';')

# do PCA on X
# add code below to instantiate the pca object
pca = PCA()
# add code below to fit the model
pcaX = pca.fit(X)

# plot tail off of components
plt.scatter(range(len(pcaX.explained_variance_)), pcaX.explained_variance_, color='#5D5166')
# plt.scatter(range(len(pcaX.components_)), pca.explained_variance_ , color='#5D5166')  
# my original line of code. It asked for explained variance vs number of components
plt.title("Tail off of Principal Components")
plt.xlabel("Index of Principal Component")
plt.ylabel("Magnitude of Eigenvalue")
plt.show()

# So now you can see that the first 25 components capture most of the variance.
