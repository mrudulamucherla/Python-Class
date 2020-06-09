'''  Please write a program to print the list after 
removing even numbers in [5,6,77,45,22,12,24]. '''


l1= [5,6,77,45,22,12,24]

new_list= [ x for x in l1 if x%2==1]
print(new_list)
