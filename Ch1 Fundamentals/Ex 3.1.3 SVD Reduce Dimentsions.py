# Use the SVD to reduce the dimensionality of X  to 25 dimensions. 
# The Data Science Officer prepared your editor with some code that has already fit the SVD. Add code to reduce X  into 25 dimensions.  


import numpy as np

# load data from csv into numpy arrays
X = np.genfromtxt('mixed-spectra-matrix.csv', delimiter=';')

# mean center X
X = X - X.mean(1)[:, np.newaxis]

# calculate svd
U, s, Vh = np.linalg.svd(X)

# get the first 25 concepts
# diagonalize s, keep only the first 25 columns
S25 = np.diag(s)[:, :25]
# keep only the first 25 rows of Vh
Vh25 = Vh[:25, :]
# use Vh25 to transform X into 25 dimensions
X25 = X.dot(Vh25.T)

# print X25 and the shape
print X25
print 'num rows, num cols\n', X25.