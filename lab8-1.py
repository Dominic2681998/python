def check(s):
    if 'ls' in s[0:2]:
        print(s)
    else:
        print('ls',s)    
s=input("Enter the data:")
check(s)
