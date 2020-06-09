''' Define a function that can receive two integral
 numbers in string form and compute their sum and 
 then print it in console. '''
 
a,b = input("enter two numbers : ").split(' ')  # values of a,b are strings   
 
def add():
    c= int(a) + int(b)
    print(c)
add()
