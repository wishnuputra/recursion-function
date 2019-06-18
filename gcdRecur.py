# -*- coding: utf-8 -*-
"""
========================================================
Greatest Common Divisor(GCD)
using recursion

Exercise of Lecture 4 MITx 6.00.1x
========================================================

This program will calculate the greatest common divisor
of two integers using recursion.

The greatest common divisor of two positive integers is 
the largest integer that divides each of them without
remainder. For example,

gcd(2, 12) = 2

gcd(6, 12) = 6

gcd(9, 12) = 3

gcd(17, 12) = 1

We use Euclid algorithm to solve this problem
recursively.

A clever mathematical trick (due to Euclid) makes it
easy to find greatest common divisors. Suppose that
a and b are two positive integers:

If b = 0, then the answer is a
Otherwise, gcd(a, b) is the same as gcd(b, a % b)

Created on Tue Jun 18 16:08:48 2019

@author: Wishnuputra
========================================================

Created on Tue Jun 18 16:08:46 2019

@author: Wishnuputra
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common
    divisor of a & b.
    '''
    # base case
    if a == 0:
        return b
    elif b == 0:
        return a
    
    # recursive case
    else:
        result = gcdRecur(b, a % b)
    
    return result
        
print(gcdRecur(17, 12))
    