#Apply SVD to the data set and determine a reasonable number of components to keep by plotting the explained variance as a function of the number of principal components. 
#The Data Science Officer prepared your editor with some code. Add code to mean center the data matrix X . Then calculate the SVD. Finally, tell matplotlib what arrays should be in the scatter plot to display explained variance plotted against number of components

import numpy as np
import matplotlib.pyplot as plt

# load data from csv into numpy arrays
X = np.genfromtxt('mixed-spectra-matrix.csv', delimiter=';')

# subtract the mean from all columns of X
X = X - X.mean(1)[:, np.newaxis]

# calculate svd
U, s, Vh = np.linalg.svd(X)  ### calculate the SVD of X using numpy

# sizes of matricies
print 'U\ts\tVh\n', U.shape, s.shape, Vh.shape
#U	s	Vh
#(360, 360) (360,) (1300, 1300)

# plot tail off of s
#plt.scatter(range(len(# put singular value array here)), # put singular value array here, color='#5D5166')
plt.scatter(range(len(U)),s , color='#5D5166')


plt.title("Tail off of Eigenvalues")
plt.xlabel("Index of Eigenvalue")
plt.ylabel("Magnitude of Eigenvalue")
plt.show()


#Again, the first 25 components capture most of the variance.