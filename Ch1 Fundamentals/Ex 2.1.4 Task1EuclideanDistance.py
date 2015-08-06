#Task 1 Suppose we have a vector of ones in a space 1.225 billion dimensions. What is the Euclidean distance between the vector and the origin?
#Natively you could try:
x = np.zeros(122500000)
y = np.ones(122500000)
dist = np.linalg.norm (x-y)
# but this will run out of memory
np.sqry (1.225 * 10**9) = 35000.0


