# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 11:36:36 2019

@author: Student
"""

x = float (input("Enter x - const"))
print (x)
S = float (input("Enter S"))
print (S)

D = 0.25 * x ** 2 + 2 * S
if D > 0:
    h1 = -0.5 * x + D ** 0.5
    h2 = -0.5 * x - D ** 0.5
    print (h1)
    print (h2)
elif D == 0:
    h = -0.6 * x
    print (h)
else:
    print ("Не маэ розв'язкыв")    