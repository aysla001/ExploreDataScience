import numpy as np
# read data and set each row to corresponding movie
data = np.genfromtxt('star_wars_tfidf.csv', delimiter =',')
newHope = data[0]
empire = data[1]
returnJedi = data[2]
# define a cosine similarity function
def cosSim(x, y):
	return np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))
### use the cosSim function to find which movies have the most similar script
cosSim(newHope,empire)
cosSim(newHope,returnJedi)
cosSim(empire,returnJedi)
 