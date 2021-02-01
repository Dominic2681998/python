m=int(input("Enter the percentage of marks:"))
if(m>90):
    grade='O'
elif(m>80 and m<=90):
    grade='A'
elif(m>70 and m<=80):
    grade='B'
elif(m>50 and m<=70):
    grade='C'
elif(m<50):
    grade='F'
print("Grade=",grade)                    