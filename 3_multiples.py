
"""  Print all 3 multiples from 1 to 100 
using for while loop."""


a=1
list1=[]
while a<=100:
    if a%3==0:
        list1.append(a)
    a+=1
print("multiples of 3 are :", list1)
