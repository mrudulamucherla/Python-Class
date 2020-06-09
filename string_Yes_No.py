''' Write a program which accepts a 
string as input to print "Yes" if the
 string is "yes" or "YES" or "Yes", 
 otherwise print "No". '''
 
str_val= input("enter a string : ")

if str_val == 'yes' or str_val =='YES' or str_val =='Yes':
    print("Yes")
else:
    print("No")
