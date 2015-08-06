import numpy as np

# open and read in data
with open('starWarsWordBag.csv', 'r') as crawls:
    newHope = np.array(crawls.readline().split(','))
    empire = np.array(crawls.readline().split(','))
    jedi = np.array(crawls.readline().split(','))

def jaccardIndex(A,B):
  ### define Jaccard Index function
  A = set(A)
  B = set(B)
  num = len(A.intersection(B))
  return (float(num) / (len(A) + len(B) - num))

print jaccardIndex(newHope, empire)
print jaccardIndex(newHope, jedi)
print jaccardIndex(empire, jedi)

#Jaccard distance
print 1- jaccardIndex(newHope, jedi)