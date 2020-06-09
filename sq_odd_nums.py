''' Use a list comprehension to square each odd number 
in a list. The list is input by a sequence of comma-separated
 numbers. Suppose the following input is supplied to the 
 program: 1,2,3,4,5,6,7,8,9 Then, the output should 
 be: 1,3,5,7,9   '''

vals= input( "enter numbers : ").split(',')
print(vals)

l1= [ int(x) for x in vals ]
print(l1)

list1= [k*k for k in l1 if k%2==1]
print(list1)
