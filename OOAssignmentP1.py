# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 16:02:36 2017

@author: snoel
"""

""" **************************************************
* LINE
****************************************************"""  
class Line(object):
    
    def __init__(self,coor1,coor2):
        """ handle line
            coor1 and 2 and tuples containing the coordinate of each point defined as (x,y)
        """
        self.coor1 = coor1
        self.coor2 = coor2
        pass
    
    def distance(self):
        #can use also x1,y1 = self.coor1
        xs = self.coor2[0] - self.coor1[0]
        ys = self.coor2[1] - self.coor1[1]
        return (xs**2 + ys**2)**0.5


    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return float((y2-y1))/(x2-x1)

""" **************************************************
* Cylinder
****************************************************"""      
class Cylinder(object):
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        #V=πr2h
        return 3.14 * self.radius**2 * self.height
    
    def surface_area(self):
        #A=2πrh + 2πr2
        return (2 * 3.14 * self.radius * self.height) + (2 * 3.14 * self.radius**2)

""" **************************************************
* MAIN
****************************************************"""   
# example for line

coordinate1 = (3,2)     #tuple
coordinate2 = (8,10)    #tuple

li = Line(coordinate1,coordinate2)

print(li.distance())

print(li.slope())

# example for cylinder
c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())
