#Generator function for the cube of numbers (power of 3)
#read: https://stackoverflow.com/questions/1756096/understanding-generators-in-python
#read: https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
def gencubes(n):
    for num in range(n):
        yield num**3        #instead of generating an keeping a huge list of element in memory
                            # only the last element is kept. There is no list

for x in gencubes(10):
    print(x)

"""
A list is an iterable object but is not an iterator by itself. So, ass all items in Python are object, it is possible to create
an iterator with anything ex:
"""
l = 'Bonjour'
s_iter = iter(l)
for i in range(len(l)):
    print(next(s_iter))         #next is used to go to the next element in the iteration
