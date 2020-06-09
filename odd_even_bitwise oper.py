'''
Write a program to check whether a number 
is even or odd using bitwise operator.
'''
n= int(input("enter a number :"))
if n&1==0:
    print("even number")
else:
    print("odd number")