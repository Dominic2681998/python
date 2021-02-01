n=[1,2,3,4,5,6,7,8,9,0,8,6,54]
i=0
odd=0
even=0
while (i<len(n)):
    if(n[i]%2==0):
        even+=1
    else:
        odd+=1
    i+=1
print("Total number of even numbers:",even)        
print("Total number of odd numbers:",odd)        