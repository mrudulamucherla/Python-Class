# -*- coding: utf-8 -*-
"""
Created on Sat May 16 11:14:04 2020

@author: shiva dumnawar
"""

'''  LCM (Least Common Multiple) of two numbers 
is the smallest number which can be divided
 by both numbers '''

# lcm of two numbers

a=6
b=28
i=1
while i<=a and i<=b:
    if a%i==0 and b%i==0:
        lcm= i*(a/i)*(b/i)
    
    i+=1
    
print(lcm)
