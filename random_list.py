'''  Please write a program to randomly generate
 a list with 5 numbers, which are divisible by
 5 and 7 , between 1 and 1000 inclusive.  '''

import random

l1= [ x for x in range(1,1001) if x%5==0 and x%7==0]

random_list= random.choices(l1, k=5)

print("list with random values: ",random_list)
