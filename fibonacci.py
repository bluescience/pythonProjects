# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 23:15:44 2016

@author: julia_001
"""
fib = [0, 1]
fibEven = []
i = 1
fibCheck = False
userNum = int(raw_input("Please input a number and I will generate the fibonacci sequence up to that number. (Please do not input 0 or any number that is inferior to 0) "))
while fibCheck == False:
    while fib[i] < userNum and userNum > 0:    
        fib.append((fib[i])+(fib[i-1]))
        i += 1
    else:
        while userNum <= 0:
            userNum = int(raw_input("Please input a number and I will generate the fibonacci sequence up to that number.(Please do not input 0 or any number that is inferior to 0) "))    
    fibCheck = True

if fib[-1] > userNum:
    del(fib[-1])

print(fib)

for value in fib:
    if value % 2 == 0:
        fibEven.append(value)

print(fibEven)

j = 0
fibInt = 0

while j < len(fibEven):
    fibInt += fibEven[j]
    j += 1
print(fibInt)
