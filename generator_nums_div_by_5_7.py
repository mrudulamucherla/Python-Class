''' Please write a program using generator to print 
the numbers which can be divisible by 5 and 7 between
 0 and n in comma separated form while n is input by
 console. Example: If the following n is given as 
 input to the program: 100 Then, the output of the 
 program should be: 0,35,70 '''
 
 
n= int(input( "enter n: "))
 
def generator():
    for i in range(n):
        if i%5==0 and i%7==0:
            yield i
            
nums=generator()

for i in nums:
    print(i, end= ', ')
