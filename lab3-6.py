m={1,2,3,4,5}
n={1,7,8,9,5}
if(len(m)==len(n)):
    print("Same length:",len(m))
else:
    print("Not equal length") 
if(sum(m)==sum(n)):
    print("Both sums are equal:",sum(m))
else:
    print("Sums are not equal")
if(m&n):
    print("Same values present in both")
else:
    print("Doesn't exist")    
