#Problem 1 - return the square of each elements until N number
"""
def gensquares(N):
    for x in range(N):
        yield x**2

for x in gensquares(10):
    print(x)
"""

#Problem 2 - generate random number n times as an iterator
"""
import random

def rand_num(low,high,n):
    for x in range(n):
        yield random.randint(low, high)

for num in rand_num(1,10,12):
    print(num)
"""

#Problem 3 - transform a string in a iterator

l = iter('Hello') #create an iterator with the list
try:
    while True:
        print(next(l))
except:
    pass


#Problem 4 - what is this doing
my_list = [1,2,3,4,5]

#for each item greater them 3 in my_list, generate a list and allow iteration on it
gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)
