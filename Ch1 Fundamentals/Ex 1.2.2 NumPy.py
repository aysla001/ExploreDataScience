
import numpy as np

#use the genfromtxt method we can load in data from numerous formats
data = np.genfromtxt('sample2.csv', delimiter=',', dtype = 'f8,i8,S15,S15', names=True)

#print the data to console
data

#dtype attribute to see how the data type formats load
data.dtype

#iterate through columns or to not have to hard code the column names in a script
data.dtype.names

#outputs entire contents of Field2
data['Field2']

#entire row
data[0]

data['Field0']			# Field 0 array
data['Field0'].mean()	# mean of array
data['Field0'].max()	# max of array
data['Field0'].argmax()	# find array location of the maximum element
data['Field0'][0]		# see whats in 0
data['Field0'].std()	# standard deviation of the array
data[0].min()			# min of the array (zeroth row)

