n=int(input("Enter the number:"))
s=1
print("Factors:")
while s<n:
    if(n%s==0):
        print(s,end=",")
    s=s+1    