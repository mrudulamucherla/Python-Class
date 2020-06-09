'''  Please write a program which prints all 
permutations of [1,2,3]   '''


from itertools import permutations

permtn= permutations([1,2,3])

for i in permtn:
    print(i)
