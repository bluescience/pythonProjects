# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import itertools
#import numpy
import pandas
# create dataframe witg index needed (all timeslots) and for each valid perm put in dataframe (table)

#test = [x for x in itertools.combinations('ABCD', 3)]
#print(test[0][0])
# comment here
class course:
    def __init__(self, name, time_start, time_stop, days, ):
        self.name = name
        self.time_start = time_start
        self.time_stop = time_stop
        self.days = days
english = course("English", 17, 18, "MWF")
math = course("Math", 17, 18, "MWF")
history = course("History", 8, 9, "TR")
physics = course("Physics", 11, 12, "TR")
allperm = [allperms for allperms in itertools.combinations([english, math, history, physics], 3)]
print(allperm)
time_conflict = []
#to_remove = []

for perm in allperm:
    # first loop, identifying tuples
    for i in range(0, len(perm)):
        if perm in time_conflict:
            break
        #checking values
        for j in range(i+1, len(perm)):
            # checking values
            if perm[i].time_start <= perm[j].time_start and perm[i].time_stop >= perm[j].time_start:
                if any(x in list(perm[j].days) for x in list(perm[i].days)):
                    time_conflict.append(perm)
                    break
            elif perm[i].time_start >= perm[j].time_start and perm[i].time_start < perm[j].time_stop:
                if any(x in list(perm[j].days) for x in list(perm[i].days)):
                    time_conflict.append(perm)
                    break

for perm in time_conflict:
    allperm.remove(perm)

schedule = pandas.DataFrame(data=None, index=['8-9','9-10','10-11','11-12','12-1','1-2','2-3','3-4','4-5','5-6'], columns=['M','T','W','R','F'], dtype=None, copy=False)
print(schedule)         
# time check            

# if(any) le inner most si il y a un conflict, ou je passe une variable ou je donne le i j ou le conflict a ete detected
                