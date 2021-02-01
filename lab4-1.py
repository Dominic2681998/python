s=input("Enter the string:")
if 'ing' in s:
    s=s.replace('ing','ly')
    print(s)
else:
    print(s+'ing')
