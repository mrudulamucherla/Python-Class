# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 11:14:49 2020

@author: mrudula
"""

# Python3 code to 
# rotate bits of number 

INT_BITS = 32

# Function to left 
# rotate n by d bits 
def leftRotate(n, d): 

	# In n<<d, last d bits are 0. 
	# To put first 3 bits of n at 
	# last, do bitwise or of n<<d 
	# with n >>(INT_BITS - d) 
	return (n << d)|(n >> (INT_BITS - d)) 

# Function to right 
# rotate n by d bits 
def rightRotate(n, d): 

	# In n>>d, first d bits are 0. 
	# To put last 3 bits of at 
	# first, do bitwise or of n>>d 
	# with n <<(INT_BITS - d) 
	return (n >> d)|(n << (INT_BITS - d)) & 0xFFFFFFFF
 
n = 5
d = 8

print("Left Rotation of",n,"by"
	,d,"is",end=" ") 
print(leftRotate(n, d)) 

print("Right Rotation of",n,"by"
	,d,"is",end=" ") 
print(rightRotate(n, d)) 

