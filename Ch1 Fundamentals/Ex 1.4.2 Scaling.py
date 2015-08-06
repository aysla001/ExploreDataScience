#If you know about machine learning or read the handbook entry, then you know that sometimes we give the algorithm data to learn on and then use it on different data (testing data) later, like the spam filter. This an issue if we scale the training data and the testing data separately. Scikit has a solution for this!
#MACHINE LEARNING OVERVIEW
#Machine Learning is the name for the type of techniques that use algorithms to essentially learn from data. There are two types of learning: supervised and unsupervised. Supervised is where you give the algorithm training data and the answers from which it learns. For example, classifying email as "inbox" or "spam" is where a machine learning algorithm is given examples of both kinds of email message, and then asked to check each incoming message, and sort appropriately. Conversely, unsupervised machine learning is where the algorithm is given data and is asked to learn natural relationships or patterns that exist in the data. For example, given an overhead shot of a carnival you can assign each person a point in 2-dimensional space. Now, you don't know who is with whom, so giving training data is impossible, but you could cluster the points (people) into groups that are likely to be together.

import numpy as np
import sklearn as sk
from sklearn import preprocessing
X = np.loadtxt('sample.data',delimiter=',')
#data = np.genfromtxt('sample.data', delimiter=',', dtype='f8,f8,f8,f8',names='a,b,c,d')
#X = np.array([data[x] for x in data.dtype.names])
mean = X.mean(axis=0)
stdev = X.std(axis=0)
scaler = preprocessing.StandardScaler().fit(X)

# identify scaler.mean_
scaler-mean_

# apply the generated scaler to the same data.
Xscaled = scaler.transform(X)

# check to see that if applied back to the same data, that it would scale to a mean of zero
Xscaled.mean(axis=0)

# the object scaler stores the parameters needed to perform the same scaling to new data. Load new data.
newdata = np.loadtxt('sample2.data', delimiter=',') 

#use the scaler object's transform method to scale the new data
newscaled = scaler.transform(newdata)

newscaled.mean(axis=0) #mean of new scaled new data
newscaled.std(axis=0)  #standard deviation of the scaled new data

