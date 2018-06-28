import timeit

#join allow to join a string to something else
#str(n) for n in range(100) will return all integer between 0 and 99
#the list will look like 0-1-2-3-4-5...99
#time it will help you to enhance the performance by testing your come a number of time
timeit.timeit("-".join(str(n) for n in range(100)), number=10000)
