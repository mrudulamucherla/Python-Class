'''  Define a function which can generate and
 print a tuple where the values are square of numbers 
 between 1 and 20 (both included).  '''
 
def sq_nums():
    tup = tuple(map(lambda x: x*x,range(1,21)))  # method 1
    print(tup)
    
    tup1= tuple([x*x for x in range(1,21)])      # method 2
    print(tup1)
sq_nums()
