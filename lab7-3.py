s="hello"
i=0
k=''
while i<len(s):
    if(i%2==0):
        k+=s[i]
        #n.append(s[i])
    i+=1
print("Result:",k)        