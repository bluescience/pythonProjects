# -*- coding: utf-8 -*-
"""
Created on Wed Nov 02 12:06:29 2016

@author: julia_001
"""

            
            
stats = dict(STR = 8, DEX = 8, CON = 8, INT = 8, WIS = 8, CHA = 8)
points = 27

while points > 0:
    
    print("Would you like to add a point to your D&D character's stats? (If yes, type \"0\", without quotes)")
    print("Would you like to remove a point to your D&D character's stats? (If yes, type \"1\", without quotes)")
    print("Would you like to cancel your D&D character's stat creation? (If yes, type \"2\" (or any other number really), without quotes)")
    print("You have {} points left.").format(points)
    print("Here are you current stats: {}").format(stats)
    userInput = int(raw_input("Which would you like to pick? "))
    
    if userInput == 0:
        statSelection = raw_input("Which value would you like to increase? (Choices are: STR, DEX, CON, INT, WIS, CHA) ").upper()
        #print type(statSelection), statSelection 
        while statSelection not in stats.keys():
            statSelection = raw_input("Which value would you like to increase? (Choices are: STR, DEX, CON, INT, WIS, CHA) ").upper() 

        stats[statSelection] += 1
        points -= 1
        
        if stats[statSelection] > 15:
            stats[statSelection] -= 1
            points += 1
            print("You may not have a stat higher than 15")
        elif stats[statSelection] < 8:
            stats[statSelection] += 1
            points -= 1
            print("You may not have a stat lower than 8")
        
        print(points)
        print(stats)
    elif userInput == 1:
        statSelection = raw_input("Which value would you like to decrease? (Choices are: STR, DEX, CON, INT, WIS, CHA) ").upper()

        while statSelection not in stats:
            statSelection = raw_input("Which value would you like to decrease? (Choices are: STR, DEX, CON, INT, WIS, CHA) ").upper() 
        
        stats[statSelection] -= 1
        points += 1
        
        if stats[statSelection] > 15:
            stats[statSelection] -= 1
            points += 1
            print("You may not have a stat higher than 15")
        elif stats[statSelection] < 8:
            stats[statSelection] += 1
            points -= 1
            print("You may not have a stat lower than 8")
        
    else:
        confirm = raw_input("WARNING: if you continue, all your progress will be erased. Do you wish to continue? (y or n) ").upper
        if confirm == 'Y':
            break
        