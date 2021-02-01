n=int(input("Enter the step count:"))
i=0
s=0
j=1
while i<n:
    k=0
    s=0
    while k<j:
        s=s+j
        print(s,end="\t")
        k=k+1
    print("\n")    
    j=j+1
    i=i+1    