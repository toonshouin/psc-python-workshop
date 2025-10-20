import math;

def a_circle(r):
    return math.pi * r ** 2

def a_tri(b,h):
    return 0.5 * b * h

def a_rec(w,h):
    return w * h

print(a_circle(int(input("Please enter the radius of the circle : "))))
print(a_tri(int(input("Please enter the base of the triangle : ")), int(input("Please enter the height of the triangle : "))))
print(a_rec(int(input("Please enter the width of the rectangle : ")), int(input("Please enter the height of the rectangle : "))))