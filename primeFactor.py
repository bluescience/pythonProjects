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


def isFactor(num):
     for i in range(1, num/2+1):
        if num % i == 0:
            factor = i
            yield factor


def isPrime(num):
    primeCheck = True
    for j in range(2, i/2+1):
        if i % j == 0:
            primeCheck = False
            if primeCheck == True:
                yield i

for i in isFactor(16):
    for j in isPrime(i):
        print(j)
'''
'''
def isFactor(num, i):
    global biggestPrimeFactor    
    if i < num/2 + 1:
        if num % i == 0:
            isPrime(num, i, 2)
        else:
            isFactor(num, i+1)
    else:
        print(biggestPrimeFactor)
        return 
      
  
def isPrime(num, i, j):                      
    global biggestPrimeFactor    
    if j < i/2 + 1:
        if i % j == 0:
            isFactor(num, i+1)
        else:
            isPrime(num, i, j+1)
    else: 
        biggestPrimeFactor = i
        isFactor(num, i+1)

isFactor(13195, 2)            
'''

n = 600851475143
i = 2
while i * i < n:
    while n % i == 0:
        n = n // i
    i = i + 1
print n
                
#Write code that checks if num is prime, and then if biggerNum is divisible by num, all in one.  