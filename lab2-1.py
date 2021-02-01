s=[1,-10,2,-20,3,-30,4,-40]
print("Positive Numbers:",[j for j in s if(j>=0)])
print("Square of numbers:",[i*i for i in s])
t="dominic savio"
t.split(",")
print("Vowels:",[m for m in t if(m=='a' or m=='e' or m=='i' or m=='o' or m=='u' or m=='A' or m=='E' or m=='I' or m=='O' or m=='U') ])
print("Ordinal value:",[ord(i) for i in t])
n=[2,3,23,45,4,56,78]
print("Odd numbers:",[i for i in n if(i%2!=0)])
y=int(input("Enter the future year for leap year:"))
print("Result:",[i for i in range(2020,y) if((i%4==0) and (i%100!=0) or (i%400==0))])