# -*- coding: utf-8 -*-
"""
Created on Thu Dec 01 22:21:05 2016

@author: julia_001
"""

numCheck = 600851475143
i = 1
numFactor = []
numPrime = []

while i < numCheck/2:
    if numCheck % i == 0:
        numFactor.append(i)
        print(numFactor)
    i +=1

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

numPrime.sort()
print(numPrime[-1])
