''' Write a  program to enter marks of 
     five subjets and calculate total, 
        average and percentage.
'''
m1=57  
m2=54
m3=49
m4=52
m5=45

total_marks=300  # each subject consists 60 marks

total_scored = m1+m2+m3+m4+m5

average= total_scored/5

percentage= (total_scored/ total_marks)*100

print("total scored marks :",total_scored)
print("average marks :",average)
print("percentage :",percentage )
