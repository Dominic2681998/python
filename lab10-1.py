valid=False
while not valid: 
    try:
        m=int(input("Enter the first number:"))
        n=int(input("Enter the second number:")) 
        r=m/n
        print("Result:",r)
        valid=True
    except ZeroDivisionError as z:
        print(z)
    except ValueError as v:
        print(v)
           
