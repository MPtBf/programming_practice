
from itertools import count

n = 100

numbersList = list(range(2, n+1))


for i in count(0):
    if i > int(max(numbersList)**(1/n))+1:  break
    n = numbersList[i]
    print(n)
    numbersList = list(filter(lambda x:  x == n or x % n != 0,  numbersList))


print(numbersList)


