''' Define a function which can generate a list
 where the values are square of numbers between 
 1 and 20 (both included). Then the function needs 
 to print the first 5 elements in the list. '''
 
def func():
    l1=[]
    for i in range(1,21):
        l1.append(i*i)
    print(l1[:5])
func()
