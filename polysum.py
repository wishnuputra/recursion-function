# -*- coding: utf-8 -*-
"""
=========================================================
POLYSUM
Exercise Lecture 4
MITX 6.00.1x
=========================================================

This program will calculates the polysum of a polygon of
n sides which has length s.

A regular polygon has n number of sides. Each side has
length s.

The area of a regular polygon is:  0.25∗n∗s2tan(π/n) 
The perimeter of a polygon is: length of the boundary
of the polygon.

The polysum function takes 2 arguments, n and s. This
function should sum the area and square of the perimeter
of the regular polygon. The function returns the sum,
rounded to 4 decimal places.

Created on Tue Jun 18 19:14:53 2019

@author: Wishnuputra
=========================================================
"""

import math

def polysum(n, s):
    '''
    n: Number of sides
    s: Length of side
    
    returns: Sum of the area and square of perimeter
    of the regular polygon. Sum is rounded to 4
    decimal places
    '''
    def area(n, s):
        return (0.25*n*s**2) / math.tan(math.pi/n)
    
    def perimeter(n, s):
        return n * s
    
    return round((area(n, s)
                  + perimeter(n, s)**2), 4)

print(polysum(6, 13))



