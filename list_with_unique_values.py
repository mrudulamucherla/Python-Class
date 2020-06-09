'''  With a given list [12,24,35,24,88,120,155,88,120,155],
 write a program to print this list after removing 
 all duplicate values with original order reserved.  '''

l1= [12,24,35,24,88,120,155,88,120,155]
print(l1)

unique_list=[]

for x in l1:
    if x not in unique_list:
        unique_list.append(x)

print(unique_list)
