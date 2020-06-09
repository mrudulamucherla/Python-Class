''' Write a program to generate and print another tuple 
whose values are even numbers in the given tuple
 (1,2,3,4,5,6,7,8,9,10)  '''
 
tup= (1,2,3,4,5,6,7,8,9,10)
print(tup)

tup1= tuple(filter(lambda  x: x%2==0, tup))  # method 1

print("even values ", tup1)

tup2= tuple([ x for x in tup if x%2==0])     # method 2 
print(tup2)
