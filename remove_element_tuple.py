'''Create a tuple (1,2,3,4,5,6), 
then remove element 5 from it.  '''

tup=(1,2,3,4,5,6)

print(tup)

l1=list(tup)
print(l1)

l1.remove(5)

tup1=tuple(l1)

print(tup1)
