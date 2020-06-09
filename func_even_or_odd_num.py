'''  Define a function that can accept an integer 
number as input and print the "It is an even number"
 if the number is even, otherwise print "It is an odd
 number".   '''
 
n= int(input("enter n : "))

def f1():
    if n%2==0:
        return "It is an even number"
    else:
        return "It is an odd number"
        
f1()
