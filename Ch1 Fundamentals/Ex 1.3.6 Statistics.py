import numpy as np
import scipy as sp

from scipy import stats
data = np.genfromtxt('iris.data', delimiter=',', dtype='f8,f8,f8,f8,S15',names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'type_string'])
sizeofdata, (minval,maxval), mean, variance, skew, kurtosis = stats.describe(data['petal_width'])

#provides further info of what the stats above are returning
sp.info(stats.describe)

#returns max and other data stats on petal_length
stats.describe(data['petal_length'])
# returns (150, (1.0, 6.9000000000000004), 3.7586666666666693, 3.1131794183445156, -0.2717119501716454, -1.395359302139705)

#median is not provided can be found using sp.median
sp.median(data['petal_length'])
