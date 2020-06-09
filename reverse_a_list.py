''' List1=[1,2,3,4,5,6,7,8,9], reverse 
the list in single line code '''

list1=[1,2,3,4,5,6,7,8,9]

print(list1)

rev_list1= list1[::-1]  # method 1
print(rev_list1)

list1.reverse()     # method 2

print("after reverse :",list1)
