s=input("Enter the words:")
s=s.split(",")
n=[]
i=0
j=i+1
while i<len(s):
    while j<len(s):
        if(s[i]>s[j]):
            t=s[j]
            s[j]=s[i]
            s[i]=t
        j=j+1    
    i=i+1
print(s)        