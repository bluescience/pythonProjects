# -*- coding: utf-8 -*-
"""
Created on Tue Nov 08 21:48:32 2016

@author: julia_001
"""
import random
i = 0
dadList = ["Tom", "John", "Bruce", "Emil", "Antoine", "Jose", "Bob", "Garreth", "Hector", "Charlemagne"]
fatherSonPair = []
leaveCheck = False
while leaveCheck == False:
    userInput = raw_input("Would you like to input a name to create a father-son pair? ").upper()
    if userInput == "Y" or userInput == "YES":
        sonName = raw_input("Please input a child's name: ")
        fatherSonPair.append("Father: ")
        RNGDad = random.randint(0, len(dadList)-1)
        fatherSonPair[i] += dadList[RNGDad]
        fatherSonPair[i] += ' / Son: '
        fatherSonPair[i] += sonName
        print(fatherSonPair)        
        i += 1
    else:
        leaveCheck = True
        print(fatherSonPair)    