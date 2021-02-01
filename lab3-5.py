s="hello"
n={}
for i in s:
    n[i]=n.get(i,0)+1
print(n)     
