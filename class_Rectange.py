''' Define a class named Rectangle which can be 
constructed by a length and width. The Rectangle class
 has a method which can compute the area.  '''
 
class Rectangle:
    def rect_area(self, length, width):
        area= length * width 
        return area

ar= Rectangle()

print("area :", ar.rect_area(20,15))
