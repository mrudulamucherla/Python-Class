''' Write a program which can compute the factorial 
of a given numbers. The results should be printed 
in a comma-separated sequence on a single line. '''

fact=1
n=int(input("enter n :"))

for i in range(1,n+1):
    fact=fact*i
print("factorial of {} is: ".format(n),fact) 
