# -*- coding: utf-8 -*-
"""
========================================================
Greatest Common Divisor(GCD)
using iteration

Exercise of Lecture 4 MITx 6.00.1x
========================================================

This program calculates the greatest common divisor
of two integers.

The greatest common divisor of two positive integers is
the largest integer that divides each of them without
remainder. For example,

gcd(2, 12) = 2

gcd(6, 12) = 6

gcd(9, 12) = 3

gcd(17, 12) = 1

This program find the greatest common divisor
iteratively.

The algorithm is to begin with a test value equal to
the smaller value of the two input arguments, and
iteratively reduce this test value by 1 until we
either reach a case where the test divides both a
and b without remainder, or we reach 1.

Created on Tue Jun 18 16:08:48 2019

@author: Wishnuputra
========================================================
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common
    divisor of a and b.
    '''
    if a > b:
        divisor = b
    else:
        divisor = a
    
    while divisor >= 1:
        if a % divisor == 0 and b % divisor == 0:
            break
        divisor -= 1
    
    return divisor

print(gcdIter(8, 12))