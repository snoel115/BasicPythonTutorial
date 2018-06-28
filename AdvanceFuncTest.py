"""
Problem 1
Use map to create a function which finds the length of each word in the phrase (broken by spaces) 
and return the values in a list.
The function will have an input of a string, and output a list of integers
ex of output [3, 4, 3, 3, 5, 2, 4, 6]
"""
print('\nProblem 1')
def word_lengths(phrase):
    #map(function ptr, list)
    #map return an iterator
    iterator = map(len, phrase.split())
    return list(iterator) #cast the iterator in a list

l = word_lengths('How long are the words in this phrase')
print(l)

"""
Problem 2
Use reduce to take a list of digits and return the number that they correspond to. 
Do not convert the integers to strings!

reduce(function ptr, sequence)
"""
print('\nProblem 2')
from functools import reduce
def digits_to_num(digits):
    #return reduce(lambda x,y: x+y, digits) --> return 13 but should return 34321
    return reduce(lambda x,y: x*10 + y,digits)

i = digits_to_num([3, 4, 3, 2, 1])
print('The number is: %s' %i)

"""
Problem 3
Use filter to return the words from a list of words which start with a target letter.
filter(function ptr,l list)
"""
print('\nProblem 3')
def filter_words(word_list, letter):
    return filter(lambda x:  x[0] == letter,word_list)

l = ['hello','are','cat','dog','ham','hi','go','to','heart']
i = list(filter_words(l,'h'))
print(i)

"""
Problem 4
Use zip and list comprehension to return a list of the same length where each value 
is the two strings from L1 and L2 concatenated together with connector between them. 
Look at the example output below: ['A-a', 'B-b']
"""
print('\nProblem 4')
def concatenate(L1, L2, connector):
    return  [x + connector + y for (x, y) in zip(L1, L2)]

print(list(concatenate(['A','B'],['a','b'],'-')))

"""
Problem 5
Use enumerate and other skills to return a dictionary which has the values of the list
as keys and the index as the value. You may assume that a value will only appear once in the given list.

ex {'a': 0, 'b': 1, 'c': 2}

Enumerate allows you to keep a count as you iterate through an object. It does this by returning a 
tuple in the form (count,element).
"""
print('\nProblem 5')

def d_list(L):
    retDict = {}
    for number,item in enumerate(L):
        retDict[item] = number

    return retDict

d = d_list(['a','b','c'])
print(d)

"""
Problem 6
Use enumerate and other skills from above to return the count of the number of items in the 
list whose value equals its index.
"""
def count_match_index(L):
    i = 0
    for number,item in enumerate(L):
        if number == item:
            i += 1

    return i

i = count_match_index([0,2,2,1,5,5,6,10])
print(i)