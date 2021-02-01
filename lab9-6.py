def binary(n):
    if n>=1:
        print(n%2,end="")
        return binary(n//2)
   
        
n=int(input("Enter the decimal number:")) 
binary(n)           