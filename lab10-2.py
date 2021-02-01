n=int(input("Enter the number:"))
try:
    if(n>90 and n<=100):
        print(n)
    else:
        raise ValueError('Abnormal Condition')     
except ValueError as v:
    print(v)        
