n=input("Enter the 4 digit sequence:")
s=[]
n=n.split(',')
for i in n:
   if(int(i)%5==0):
       s.append(i)
print(s)        