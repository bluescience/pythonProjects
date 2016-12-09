# -*- coding: utf-8 -*-
"""
Created on Thu Dec 01 22:21:05 2016

@author: julia_001
"""
'''
i = 1
numFactor = []
numPrime = []

def isPrimeFactor(numCheck):      
    for i in range(1, numCheck/2):
        if numCheck % i == 0:
            numFactor.append(i)
            print(numFactor)
        i +=1
    #Finding factors
        
    for factor in numFactor:
        i = 2
        primeCheck = False
        while i < factor/2:
            if factor % i == 0:
                primeCheck = True
            i +=1
    if primeCheck == False:
        numPrime.append(factor)
        print(numPrime)
    #Checking if factors are prime
    numPrime.sort()
    print(numPrime[-1])

isPrimeFactor(600851475143)
'''

def isPrimeFactor(num):
     for i in range(1, num/2):
        if num % i == 0:
            primeCheck = True
            for j in range(2, i/2):
                if i % j == 0:
                    primeCheck = False
            if primeCheck == True:
                biggestPrimeFactor = i
                print(biggestPrimeFactor)
     print(biggestPrimeFactor)

isPrimeFactor(600851475143)
                
        
        

#Write code that checks if num is prime, and then if biggerNum is divisible by num, all in one.  
            