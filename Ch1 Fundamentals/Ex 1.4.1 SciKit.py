#scikit-learn, scikit imported as sklearn is a machine learning library that is built on top of NumPy, SciPy, and matplotlib. 

#scaling data
import numpy as np
import sklearn as sk
from sklearn import preprocessing
data = np.genfromtxt('sample.data', delimiter=',', dtype='f8,f8,f8,f8',names='a,b,c,d')
#this method of import creates a flexible type which does not allow `mean.()` to be called
X = np.array([data[x] for x in data.dtype.names])
mean = X.mean(axis=0)
stdev = X.std(axis=0)

mean
#will return the mean of each column

#preprocessing subtracts the mean and divides by the standard deviation
scaledData = preprocessing.scale(X)

# mean of scaledData
scaledData.mean(axis=0)
# standard deviation of scaledData
scaledData.std(axis=0)