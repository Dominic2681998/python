#Area of rectangle
l=int(input("Enter the length of rectangle:"))
b=int(input("Enter the breadth of rectangle:"))
rectangle=lambda x,y:x*y
print("Area of rectangle:",rectangle(l,b))
#Area of square
a=int(input("Enter the side of the square:"))
square=lambda x:x*x
print("Area of the square:",square(a))
#Area of the triangle
br=int(input("Enter the base of triangle:"))
h=int(input("Enter the height of triangle:"))
triangle=lambda x,y:0.5*br*h
print("Area of triangle:",triangle(br,h))