# -*- coding: utf-8 -*-
"""
Created on Sat May 16 12:06:16 2020

@author: shiva dumnawar
"""

l1=[] 
n= int(input("enter no. of values :"))         
for i in range(n):
    num=int(input("enter values :")) 
    l1.append(num)

print(l1)      #l1=[5,12,4,8,4,1,5,3,5]


from collections import Counter

x=Counter(l1)

print(x)

l2=x.most_common(2)
print(l2)

sec_num= l2[1][0]

print("second most frequent number :",sec_num)









