#Largest value
a,b=10,20
largest=lambda x,y:max(a,b)
print(largest(a,b))
#Divisible by 5
n=int(input("Enter the number:"))
check=lambda x:print("Divisible by 5") if n%5==0 else print("Not divisible by 5")
check(n)
#check length of string greater than 5
S=["Hi","python","programming","hey"]
leng=list(filter(lambda x:len(x)>5,S))
print(leng)
#To increment a list of integers by 10% if the number is greater than 1000 else by 5%.
d=[1001,999,1005,121]
incr=list(map(lambda x:x+x*.1 if x>1000 else x+x*0.5,d))
print(incr)