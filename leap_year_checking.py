''' Write a program to check whether a given
 year is leap year or not
 using conditional operator.
'''
year= int(input("enter a year :"))
def year_check():
    if year%100==0:
        if year%4==0 and year%400==0:
            print("It's a Leap year")
        else:
            print("It's a Normal year")
    elif year%4==0:
        print("It's a Leap year")
    else:
        print("It's a Normal year")
year_check()