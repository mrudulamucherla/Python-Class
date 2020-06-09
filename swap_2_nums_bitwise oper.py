''' 
Write a program to swap two 
    numbers using bitwise operator.
'''

a=56
b=20
print("a :",a)
print("b :",b)
a=a^b
b=a^b
a=a^b
print("after swapping")
print("a :",a)
print("b :",b)