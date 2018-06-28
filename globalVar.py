# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 23:36:00 2017

@author: snoel
"""

toto = 0

def abc():
    global toto
    toto = 1
    
print(toto)
abc()
print(toto)

