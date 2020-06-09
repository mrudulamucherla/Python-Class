# -*- coding: utf-8 -*-
"""
Created on Sat May 16 10:45:11 2020

@author: shiva dumnawar
"""


# Gcd or Hcf of two numbers

def gcd_rec(a,b):
    if b==0:
        return a
    else:
        return gcd_rec(b, a%b)
     
k=gcd_rec(54,4)
print("gcd of a and b :",k)
