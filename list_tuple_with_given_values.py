''' 	Write a program which accepts a sequence of 
comma-separated numbers from console and generate a 
list and a tuple which contains every number.   '''

nums= input("enter numbers : ").split(',')

list1= [x for x in nums] 
print("list1 : ", list1)

tup= tuple([k for k in nums])
print("tup : ", tup)
