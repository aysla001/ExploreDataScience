#Take a look at the original data, the random projection data, and the final LSH.
#APPLYING LSH IV
#Use Python and the console to answer the following questions.

#Print the original data, data. What is the only non-zero value that appears in the subset of the data displayed?

import numpy as np
from sklearn import random_projection
# load data from csv into numpy arrays
data = np.genfromtxt('mixed-spectra-matrix.csv', delimiter=';')
# apply a Gaussian random projection
tx = random_projection.GaussianRandomProjection(n_components = 25, random_state = 1)
data25 = tx.fit_transform(data)
# now convert every element x into 0 if x < 0 and 1 if x >= 0
# first define a transformation function to apply to each element
def tx01(x):
	return 0 if x < 0 else 1
# apply tx01 to each element using vectorize
vtx01 = np.vectorize(tx01)
data01 = vtx01(data25)
