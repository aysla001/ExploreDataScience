
import numpy as np

# ignore the strings in out CSV and just work with the numbers
# set skiprows arguement to skip headers
data2 = np.loadtxt('sample2.csv', delimiter=',', usecols=(0,1), skiprows=1) 

# lets look at the data
data2
#array([[ 3.14159   ,  0.        ],
#       [ 2.71828   ,  1.        ],
#       [ 0.577215  ,  2.        ],
#       [ 0.20787958,  3.        ]])

# accessing the rows is the same, but columns is not. We don't have a field to identify
data2.transpose()
#from there we can access a column as a row. store as a variable. then call like you would an array. x[0]
#array([[ 3.14159   ,  2.71828   ,  0.577215  ,  0.20787958],
#       [ 0.        ,  1.        ,  2.        ,  3.        ]])

# another option is to unpack the data as it comes in
# load data into x and y, then print x
x,y = np.loadtxt('sample2.csv', delimiter=',',usecols=(0,1),skiprows=1 unpack=True)
x #print results. See below
# array([ 3.14159   ,  2.71828   ,  0.577215  ,  0.20787958])