# -*- coding: utf-8 -*-
"""
Created on Tue Dec 06 23:18:42 2016

@author: julia_001
"""

firstInt = 100
secondInt = 100
biggestPalindrome = 0
op = 0

while firstInt < 1000:
    secondInt = 100
    while secondInt < 1000:
        op = (firstInt * secondInt)
        if str(op) == str(op)[::-1] and op > biggestPalindrome:
            biggestPalindrome = (op)
        #print("{} x {} = {}").format(firstInt, secondInt, op)
        #print("Current biggest palindrome is {}.").format(biggestPalindrome)
        secondInt += 1
    firstInt += 1
print(biggestPalindrome)