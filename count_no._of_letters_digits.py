'''   Write a program that accepts a sentence and calculate 
the number of letters and digits. Suppose the following input 
is supplied to the program: hello world! 123 Then, the output 
should be: LETTERS 10 DIGITS 3   '''

txt= input("enter a sentence: ")
print(txt)
  
letters=0
digits=0

for i in txt:
    if i.isalpha() == True:
        letters+=1
    elif i.isdigit() == True: 
        digits+=1
    else:
        pass

print("letters ", letters)
print("digits ", digits)
