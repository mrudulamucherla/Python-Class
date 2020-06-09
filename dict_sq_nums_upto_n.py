'''  With a given integral number n, write a program to 
generate a dictionary that contains (i, i*i) such that it is an 
integral number between 1 and n (both included). and then the
 program should print the dictionary.   '''
 
 
dic={}
n= int(input("enter a number: "))
for i in range(1, n+1):
    dic.update({i: i*i})
    
print(dic)
