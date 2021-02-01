n=int(input("Enter the first number:"))
m=int(input("Enter the second number:"))
if(n<m):
    s=n
    k=m
else:
    s=m
    k=n
while s>0:
    if(k%s==0):
        print("GCD:",s)
        break
    else:
        s=s-1    
