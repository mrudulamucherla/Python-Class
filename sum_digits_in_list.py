'''  Write a program that computes the value of
 a+aa+aaa+aaaa with a given digit as the value of a. 
 Suppose the following input is supplied to the program: 9 
 Then, the output should be: 11106  '''

v= 'a+aa+aaa+aaaa' 
a_val= input("enter value ")  #string

s=v.replace('a',a_val) 

print(s)

l1= [ int(x) for x in s.split('+')]
print(l1)

print("sum", sum(l1))
