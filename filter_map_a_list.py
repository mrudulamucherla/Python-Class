'''  Write a program which can map() and filter() 
to make a list whose elements are square of even number
 in [1,2,3,4,5,6,7,8,9,10].   '''


l1= [x for x in range(1,11) ]
print(l1)

even_nums= list(filter(lambda x: x%2==0, l1))
print(even_nums)

sq_nums= list(map( lambda x: x**2, even_nums))
print(sq_nums)
