''' Create a dictionary with following 
tuples (1,2), (2,3), (3,4). '''

tup=(1,2),(2,3),(3,4)

print(tup)

dic={}

for i, j in tup:
    dic.update({i:j})

print(dic)
