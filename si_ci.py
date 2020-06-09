# -*- coding: utf-8 -*-
"""
Created on Fri May 15 15:16:21 2020

@author: shiva dumnawar
"""
# simple interest

p=12500     # p : principal
t=2         # t :  time in years
r=8        # r : rate of interest

def simple_int():
    si= (p*t*r)/100    # si : simple interest
    print("simple interest : ", si)

simple_int()

#compound interest

def comp_int():
    ci= p*((1+(r/100))**t-1)  # ci : compound interest
    print("compound interest :",ci)

comp_int()
