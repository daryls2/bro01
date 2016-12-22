# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 07:56:32 2016

@author: Daryl
"""

def calcmax(wgt, reps, xreps):
    # First calculate one rep max
    if 0 < reps < 10:
    # Brzycki - Use for 1-9 reps
        max1r= wgt*(36/(37-reps))        
    elif 9 < reps < 21:
        #Epley - Use for reps 10+
        max1r=wgt*(1+(reps/30))
    else:
        max1r = 0
        
        
    if 0 < xreps < 10:
        maxxr = max1r/(36/(37-xreps))
    elif 9< xreps < 21:
        maxxr = max1r/(1+(xreps/30))
    else:
        maxxr = 0
        
    return round(maxxr,1)

wgt = float(input("Weight lifted: "))
reps = int(input("Number of reps performed: "))
xreps = int(input("Enter rep max to calculate: "))
xwgt = calcmax(wgt, reps, xreps)
#1print (calcmax(wgt,reps,xreps))
print(xwgt)


    
