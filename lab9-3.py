def sum(n):
    if n==0:
        return n
    else:
        return n%10 +sum(n//10)  
n=int(input("Enter the number:"))
print("Sum:",sum(n))