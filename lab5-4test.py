import math
u=int(input("Enter the lower boundary:"))
l=int(input("Enter the upper boundary:"))
while (u<=l):
    s=math.sqrt(u)
    if(s-math.floor(s)==0):
        t=str(u)
        if(int(t[0])%2==0 and int(t[1])%2==0 and int(t[2])%2==0 and int(t[3])%2==0):
            print(t)
    u=u+1        