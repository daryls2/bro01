# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def round2place(wgt, round2place):
    ''' 
    This will return a weight rounded to the nearest
    round2place pound  - EX: 
        round2place = 5
        332 would round to 330
        333 would round to 335
    '''
    x = round(wgt * (1.0/round2place),0)*round2place
    return x


wgt = 333
roundplace = 5

y=round2place(wgt, roundplace)
print(y)

startwgt = 135
workwgt = 350
warmsets = 5

wgtstep = (workwgt-startwgt)/warmsets

for i in range(warmsets+1):
    #print(startwgt+(i*wgtstep))
    print(round2place(startwgt+(i*wgtstep),5))
