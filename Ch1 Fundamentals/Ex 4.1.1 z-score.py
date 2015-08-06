#calculate z-score using numpy

import numpy as np
data = np.loadtxt('seeds_dataset.txt')
isone = data[:,7]==1
data1 = data[isone,:]
zdata = (data1[:,0] - np.mean(data1[:,0])) / np.std(data1[:,0])
print zdata


# the other way calculate z-score
import scipy.stats as stats
zareaB = stats.mstats.zscore(data1[:,0])
zdata1 = stats.mstats.zscore(data1)
