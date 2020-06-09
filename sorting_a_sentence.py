''' Write a program that accepts a sequence of 
whitespace separated words as input and prints 
the words after removing all duplicate words and 
sorting them alphanumerically. '''

words= input("enter words : ").split(' ')
print(words)
print(' '.join(sorted(set(words))))
