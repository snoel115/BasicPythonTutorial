
"""
Problem 1: Convert 1024 to binary and hexadecimal representation:
"""
print('\nProblem 1')
print(bin(1024))
print(hex(1024))

"""
Problem 2: Round 5.23222 to two decimal places
"""
print('\nProblem 2')
print(round(5.23222, 2))

"""
Problem 3: Check if every letter in the string s is lower case
"""
s = 'hello how are you Mary, are you feeling okay?'
print('\nProblem 3')
print(s.islower())

"""
Problem 4: How many times does the letter 'w' show up in the string below?
"""
print('\nProblem 4')
s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print(s.count('w'))

"""
Problem 5: Find the elements in set1 that are not in set2:
"""
print('\nProblem 5')
set1 = {2,3,1,5,6,8,9}
set2 = {3,1,7,5,6,8}
set3 = set1.difference(set2)
print(set3)

"""
Problem 6: Find all elements that are in set1 and not in set 2:
"""
print('\nProblem 6')
set1 = {2,3,1,5,6,8,9}
set2 = {3,1,7,5,6,8}
set3 = set1.intersection(set2)
print(set3)

"""
Problem 7: Create this dictionary: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64} using dictionary comprehension
"""
print('\nProblem 7')
d = {x:x**3 for x in range(5)}
print(d)

"""
Problem 8: Reverse the list below:
"""
print('\nProblem 8')
l = [1,2,3,4]
l.sort(reverse=True)
print(l)

"""
Problem 9: Sort the list below
"""
print('\nProblem 9')
l = [3,4,2,5,1]
l.sort()
print(l)