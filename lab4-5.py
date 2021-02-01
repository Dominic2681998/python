s=input("Enter the string:")
if 'not bad' in s:
    s=s.replace('not bad','good')
    print(s)  
elif('bad not' in s):
    n=s.index('bad not')
    print("First appearance:",n+1)

  
