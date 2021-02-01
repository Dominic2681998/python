s="hello hello how how are you"
n={}
for j in s.split():
    n[j]=n.get(j,0)+1
print(n)    
    