s=input("Enter the string:")
s=s.split()
t=s[0]
for n in s:
    if len(t)>len(n):
        m=s.count(t)
        h=t
    else:
        t=n
        h=t
if(m>1):
    print("Bingo")     
else:
    print("Longest:",h)           
