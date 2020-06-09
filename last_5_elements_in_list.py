''' Define a function which can generate a list 
where the values are square of numbers between 
1 and 20 (both included). Then the function 
needs to print the last 5 elements in the list. '''

def list1():
    l1=[x**2 for x in range(1,21)]
    print("list :", l1)
    print("last 5 elements :", l1[-5:])
    
list1()
