# -*- coding: utf-8 -*-
"""
======================================================
Find If Character is in String
Exercise of Lecture 4 MITx 6.00.1x
======================================================

This program check whether a string contain the 
character that we specify. If it contains the
character return True, if not return False.

We assume that the string that we passed is in
alphabetical order. Then we uses bisection search
method to find if the charcter exists in the
string.

Created on Tue Jun 18 19:14:53 2019

@author: Wishnuputra
======================================================
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == "":
        return False
    
    midIndex = len(aStr) // 2
    midChar = aStr[midIndex]
    halfStr = ""

    # base case
    if char == midChar:
        return True
    
    # recursive case
    else:
        if char > midChar:
            halfStr = aStr[midIndex+1:]
        else:
            halfStr = aStr[:midIndex]
        return isIn(char, halfStr)
    
print(isIn('s', "abbhiijjlmmopqrsvy"))


