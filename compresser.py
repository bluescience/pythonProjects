# -*- coding: utf-8 -*-
"""
Created on Wed Nov 09 11:32:03 2016

@author: julia_001
"""
#Program compresses a string
beep = "beeeeeeeep"
beepList = list(beep) # casts the string for easier manipulation
beepCompression = [] # creates list for manipulation

i = 1
startSplitCheck = 0 #Creates iterator variable and a variable for easier splitting
beepList.append("")
for c in list(range(len(beepList)-2)): #Iterates through the list for compression

    print("I am at index {}").format(i)
    print("I am at letter {}").format(beepList[i])
    if beepList[i-1] != beepList[i]:# or beepList[i] == beepList[14]: # checks if value can not be compressed
        #split the list into a compressed format: ie turn 'eeep' into 3e1p
        beepCompression.append(len(beepList[startSplitCheck : i]))
        beepCompression.append(beepList[i-1])
      #  if startSplitCheck == 0:
       #     beepCompression[0] += 1
        startSplitCheck = i
        i += 1
    
    else: #goes here if value can be compressed
        i += 1
        

beepCompression.append(len(beepList[startSplitCheck : i]))
beepCompression.append(beepList[i-1])

print(beepCompression)