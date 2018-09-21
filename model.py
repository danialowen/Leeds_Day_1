# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 15:59:06 2018

@author: gydwo
"""


import random

y0 = 50
x0 = 50

if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1

if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1
    
if random.random() < 0.5:
    y0 += 1
else:
    y0 -= 1

if random.random() < 0.5:
    x0 += 1
else:
    x0 -= 1

print(y0, x0)




y1 = 50
x1 = 50

if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1

if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1
    
if random.random() < 0.5:
    y1 += 1
else:
    y1 -= 1

if random.random() < 0.5:
    x1 += 1
else:
    x1 -= 1

print(y1, x1)


#MATHS
dist_y = (y1-y0)**2 
dist_x = (x1-x0)**2
answer = (dist_y + dist_x)**0.5
print (answer)


#For random number between more than 0 and 1
#can't use random.random() - use random.randint(0,... e.g. 99)