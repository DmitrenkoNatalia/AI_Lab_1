# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 11:23:43 2019

@author: Student
"""

y = int(input())
if y % 4 == 0 and y % 100 != 100:
    print ("YES")
elif y % 400 == 0:
    print ("YES")
else:
    print ("NO")