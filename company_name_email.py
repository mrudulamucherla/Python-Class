''' Print The Company Name Of A Given Email Address
 If the following email address is given as input
 to the program: john@google.com Then, the 
 output of the program should be: google
 '''

email= input("enter your email ")
print("email ", email)

print("company name ", email[ email.index('@')+1: -4])
