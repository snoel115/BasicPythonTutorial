# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 15:32:40 2017

@author: snoel
"""
""" ***************************************************
Animal Class
    This is the base Class
****************************************************"""
class Animal(object):
    species = 'Not yet define'
    
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")
 
""" ***************************************************
Dog Class
    note, this class hinerit from the Animal Class
****************************************************"""       
class Dog(Animal):
    
    #class object attribute
    species = 'mammal'
    
    def __init__(self, sName = 'New Name', sType = 'Golden Retreaver', iAge = 0):

        Animal.__init__(self) #initialize the base class
        
        self.name = sName
        self.typeof = sType
        self.age = iAge

        print("Dog created")

    #overwrite teh whoAmI method for the dog
    def whoAmI(self):
        print("Dog")

    def bark(self):
        print ("Woof!")
    
    #overwrite the "str" python function
    #NOTE: the overwrite MUST return the same type as they original python method
    def __str__(self):
        return "Name: %s, Type: %s, Age: %s " %(self.name, self.typeof, self.age)


""" ***************************************************
MAIN function
****************************************************"""
print('\nPRINT ABOUT DOG /W PARAMETERS')
empty = Dog()                           #without any parameters
print(empty)
print('Empty is %s years old' %(empty.age))

print('\nPRINT ABOUT CHARLIE')
charlie = Dog(sName = 'Charlie', iAge = 3) #assign specific parameters
print(charlie)
print('Charlie is %s years old' %(charlie.age))

print('\nPRINT ABOUT SAM]')
sam = Dog('Samuel', 'German Shappard', 2.5) #assign all parameters
sam.whoAmI()
print(sam)
print('%s is %s years old and is a %s' %(sam.name, sam.age, sam.species))

#print(Animal(sam.species))
