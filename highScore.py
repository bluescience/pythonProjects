# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 15:27:45 2016

@author: julia_001
"""



highScore = []
tempHighScore = []


menuCheck = True

while menuCheck == True:
    count = 0
    
    print("\nHIGH SCORE RECORDER\n")
    print("0 - quit")
    print("1 - input new high score")
    print("2 - sort high scores")
    mainMenuChoice= raw_input("Please input one of these numbers: ")
    while mainMenuChoice.isdigit() == False:
        print("Please make sure the number you inputed is only composed of numbers: ")
    if mainMenuChoice == 0:
        menuCheck = False  
        
    elif mainMenuChoice == 1:
        name = raw_input("Please input your name: ")
        tempHighScore.append(name)
        userHighScore = raw_input("Please input your high score: ")
        while userHighScore.isdigit() == False:
            userHighScore = raw_input("Please make sure the number you inputed is only composed of numbers: ")    
        tempHighScore.append(userHighScore)
        
        highScore.append(tempHighScore[0:2])
        del(tempHighScore[0:2])
        
        
        
    elif mainMenuChoice == 2:
        highScore.sort(key=lambda x: int(x[1]))
        highScore.reverse()
        print("0. [name, highscore]")
        for x in highScore:
            count +=1
            print("{}. {}").format(count, x) 
        
    else:
        print("Please input a valid number. \n")