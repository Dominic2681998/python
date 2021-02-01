class MyException (Exception): 
   pass
username="test123"
password=1234
try:
    u=input("Enter the username:")
    p=input("Enter the password:")
    if u==username and p==password :
        print("Success")
    else:
        raise MyException("Invalid user")
except MyException as m:
    print(m)              