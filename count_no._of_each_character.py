'''  Please write a program which count and print the
 numbers of each character in a string input by console.  '''
 
from collections import Counter 

txt = input("enter a string: ")

print(Counter(txt))
