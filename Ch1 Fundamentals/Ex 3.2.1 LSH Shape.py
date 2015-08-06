#Objective 1
#Use a NumPy array command to print the number of rows and columns and use that information to answer the following questions.
#shape command

import numpy as np
from sklearn import random_projection

# load data from csv into numpy arrays
data = np.genfromtxt('mixed-spectra-matrix.csv', delimiter=';')
print(data.shape)
