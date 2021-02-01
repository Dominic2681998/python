def reverse(s):
    if len(s)==1:
        return s
    else:
        return s[-1]+reverse(s[:-1])
s=input("Enter the string:")
print("Reversed string:",reverse(s))            