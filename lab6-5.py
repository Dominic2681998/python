s=input("Enter the data:")
count=0
v='aeiou'
for i in s:
    if i.lower() in v:
        count+=1
print("Vowels:",count)      
