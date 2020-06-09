'''  Print all 3 multiples from 1 to 100
 using for loop. '''
 
list1=[]

for i in range(1,100):
    if i%3==0:
        list1.append(i)
print("multiples of 3 :", list1)
