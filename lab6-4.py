n=input("Enter the list of integers:")
n=n.split()
s=[]
for i in n:
    if(int(i)>100):
        s.append('over')

    else:
        s.append(i)    
print(s)    
