count=0
l=[1,1,2,3,4,1,4,1,5]
t=1
i=0
while i<len(l):
    if(l[i]==t):
        count+=1
    i=i+1    
print("Total count:",count)        