'''   Define a class with a generator which can iterate the
 numbers, which are divisible by 7, between a given range 0 and n.
 Hints: Consider use yield '''
 
class generator:
    def ss(self, n):
        for i in range(n):
            if i%7==0:
                yield i
                
mul_7= generator()
k=mul_7.ss(40)

for val in k:
    print(val)
