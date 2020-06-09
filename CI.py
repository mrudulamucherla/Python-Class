'''  Write a  program to enter P, T, R and 
       calculate compound Interest.
'''

P= int(input("enter principal amount: "))
T = int(input("enter time :"))
R = float(input(" rate of interest :"))
CI= (P*(1+(R/100))**T)-P
print("compound interest :",CI)