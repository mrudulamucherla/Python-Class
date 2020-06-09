''' Define a function which can generate 
and print a list where the values are 
square of numbers between 1 and 20 
(both included). '''

def sq_nums():
    l1=[]
    for i in range(1,21):
        l1.append(i*i)
    print(l1)

sq_nums()
