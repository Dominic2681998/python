try:
    try:
        n=int(input("Enter the number:"))
        if(n<0):
            raise ValueError("Unexpected error")
    except ValueError as v:
        print(v)
        raise
    else:
        print("Greater than zero")
except ValueError as va:
    print("Re-raised exception:",va)

#Assertions
try:
    m=int(input("Enter the first number:"))
    n=int(input("Enter the second number:"))
    assert n>0,"Division by zero"
    print("Result:",m/n)
except AssertionError as a:
    print(a)        
        
