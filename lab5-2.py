n=int(input("Enter the count:"))
a=0
b=1
i=1
print("Fibonacci:")    
print(a)
print(b)
while i<n-1:
    s=a+b
    a=b
    b=s
    i=i+1
    print(s)

