'''  Define a function which can print a dictionary 
where the keys are numbers between 1 and 3 
(both included) and the values are square of keys.'''

def dict1(n):
    dic={}
    for i in range(1, n+1):
        dic.update({i:i*i})
    print(dic)
dict1(3)
