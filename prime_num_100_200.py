# -*- coding: utf-8 -*-
"""
Created on Sat May 16 15:23:22 2020

@author: shiva dumnawar
"""

prime_nums=[]

for i in range(100,200):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        prime_nums.append(i)
        
print(prime_nums)
            