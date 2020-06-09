'''   Define a function that can accept two strings as input 
and print the string with maximum length in console.
 If two strings have the same length, then the function 
 should print all strings line by line.   '''
 
a,b= input(" enter two strings: " ).split(' ')

def str_max():
 
    if len(a)> len(b):
        print("string with max length is :", a)
    elif len(b)> len(a):
        print("string with max length is :", b)
    else:
        print("both have same length")
        print( a)
        print( b)
    
str_max()  
