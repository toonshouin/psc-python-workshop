import math

def calculate_areas():
    print("Circle area:", math.pi * int(input("Enter radius: ")) ** 2)
    print("Triangle area:", 0.5 * int(input("Enter base: ")) * int(input("Enter height: ")))
    print("Rectangle area:", int(input("Enter width: ")) * int(input("Enter height: ")))

calculate_areas()