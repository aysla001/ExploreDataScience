import numpy as np
# read in data, skip the last column which contains class labels
data = np.genfromtxt('Jedi.data', delimiter=',', usecols=range(4))
### now calculate the covariance matrix of data
np.cov(data, rowvar=0)

#inverse of covariance matrix
a = np.cov(data, rowvar=0)
np.linalg.inv(a)
  