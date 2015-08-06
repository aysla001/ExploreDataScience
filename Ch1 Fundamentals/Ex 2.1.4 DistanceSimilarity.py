import numpy as np
np.random.seed(1000)
# generate a list of random vectors
x = [np.random.rand(1,50) for _ in range(50)]
# set z equal to the origin
z = np.zeros(50)
### find the distance between all x_i and z and find the min of those distances
for i in z:
	d=np.linalg.norm(x-z)

d = [np.linalg.norm(y - z) for y in x]

min(d)