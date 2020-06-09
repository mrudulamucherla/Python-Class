'''  Please write a program to shuffle and print the 
list [3,6,7,8].  '''

import random

l1= [3,6,7,8]

random.shuffle(l1)    # method :1  it shuffles original list
print("list after shuffling ", l1)

shuffled_list= random.sample(l1,len(l1))  # method :2 it creates a new list with shuffled values 

print("shuffled list", shuffled_list)
