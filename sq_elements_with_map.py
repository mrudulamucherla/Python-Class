'''  Write a program which can map() to make a list whose 
elements are square of numbers between 1 and 20
 (both included).  '''
 
l1= list(range(1,21))
print(l1)
sq_nums= list(map( lambda x: x**2, l1))
print(sq_nums)
