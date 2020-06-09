''' Please write a program to generate 
a list with 5 random numbers between 
100 and 200 inclusive.  '''

import random 

l1= random.choices(range(100,201), k=5)
print(l1)   
