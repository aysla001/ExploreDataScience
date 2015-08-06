 import numpy as np
# read in data, skip the last column which contains class labels
data = np.genfromtxt('Jedi.data', delimiter=',', usecols=range(4))
# calculate the inverse covariance matrix
invCov = np.linalg.inv(np.cov(data, rowvar=0))
# get the first and second observation
x = data[0]
y = data[1]
# use x, y, and invCov to calculate the Mahalanobis distance
np.sqrt((x - y).T.dot(invCov).dot(x - y))