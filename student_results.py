# Students Results	

marks=int(input("enter marks :"))
print(marks)

if marks>=0 and marks<=100:
    if marks > 70:
        print("distinction")
    elif marks>60 and marks<70:
        print("first class")
    elif marks>50 and marks<60:
        print("second class")    
    elif marks>40 and marks<50:
        print("third class")
    elif marks<40:
        print("fail")
else:
    print("enter marks between 0 and 100")
