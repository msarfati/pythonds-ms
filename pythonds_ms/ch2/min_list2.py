# Find the minimum in a list
from pprint import pprint
from random import randrange
#l = [9, 3, 2, 0, 22, -4]
l = [randrange(100) for i in range(10)]

minimum = l[0]
for i in l:
    minimum = i if minimum > i else minimum

pprint(l)
print(minimum)
