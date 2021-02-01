import graphics.rectangle,graphics.circle
from graphics.dgraphics import cuboid as c
from graphics.dgraphics.sphere import *
l=int(input("Enter the length of rectangle:"))
b=int(input("Enter the breadth of rectangle:"))
print("Area of rectangle:",graphics.rectangle.area_rectangle(l,b))
print("Perimeter of rectangle:",graphics.rectangle.perimeter_rectangle(l,b))
#Working with circle
r=int(input("Enter the radius:"))
h=int(input("Enter the height:"))
print("Area of circle:",graphics.circle.area_circle(r))
print("Perimeter of circle:",graphics.circle.perimeter_circle(r,h))
#Working with cuboid
l=int(input("Enter the length of cuboid:"))
b=int(input("Enter the breadth of cuboid:"))
h=int(input("Enter the height of cuboid:"))
print("Area of circle:",c.area_cuboid(l,b,h))
print("Perimeter of circle:",c.perimeter_cuboid(l,b,h))
#Working with sphere
r=int(input("Enter the radius of the sphere:"))
print("Area of sphere:",area_sphere(r))
print("Circumference of sphere:",perimeter_sphere(r))

