# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 22:49:23 2017

@author: snoel
"""

"""*****************************************
* Problem 1
*****************************************"""
def Problem1():
    i = 0
    while i <= 10: 
        try:
            for c in ['a','b','c']:
                print (c**2)        # this will always fail as a character can't be converted in int 
        except TypeError:
            print('An error occur')
        finally:
            print('The value of %s is: ' %i)
            i += 1


"""*****************************************
* Problem 2
*****************************************"""
def Problem2(x, y):

    z= 0

    try:
        z = x/y
    except ZeroDivisionError:
        print('The devider is 0, so the division failed')
    else:
        print('An error occured')
    finally:
        print('Thank you!')
        print('the result is %s' %z)
        

"""*****************************************
* Problem 3
*****************************************"""
def Problem3():

    i = 0
    while True:
        try:
            i = int(input('Input an integer: ' ))
            i = i**2
        except ValueError:
            print('The value entered is not an integer')
            print('Try again')
            continue
        else:
            print('An unknown error occured')
        finally:
            print('Thank you, your number squared is: %s' %i)
            break

"""*****************************************
* MAIN
*****************************************"""
#Problem1()
#Problem2(5, 3)
Problem3()