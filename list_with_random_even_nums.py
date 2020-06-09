'''  Please write a program to randomly generate a list
 with 5 even numbers between 100 and 200 inclusive. '''
 
import random 

even_numbers= random.choices(range(100,201,2), k=5)
print(even_numbers)   
