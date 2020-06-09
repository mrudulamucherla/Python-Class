
'''Create a list and remove last element
 from it.'''
 
list1=[12,28,67,158,59]

print(list1)

list1.remove(59)  # remove()
print(list1)

list1.pop()  # pop removes last element
print(list1)

del list1[-1]  # del 
print(list1)
