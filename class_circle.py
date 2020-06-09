'''  Define a class named Circle which can be
 constructed by a radius. The Circle class has a method 
 which can compute the area. '''
 
from math import pi

class circle:
    def ar(self, r):
        area= pi * r * r
        print( "area of circle : " , area)
    
cir_area= circle()
cir_area.ar(24)
