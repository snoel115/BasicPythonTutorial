# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 15:32:40 2017

@author: snoel
"""

class Dog(object):
    
    # Class Object Attribute
    species = 'mammal'
    
    def __init__(self, breed = 'Golden Retreaver', name = 'Charlie'):
        self.breed = breed
        self.name = name
        
    
charlie = Dog()
sam = Dog('Lab','Sam')
print('Charlie is a : ' + charlie.breed)
print('Sam is a :' + sam.breed)