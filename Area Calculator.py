import math

while True:
    print()
    print("Area Calculator")
    print()
    print("1. Square")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Circle")
    print()

    choice = float(input("Enter you choice: "))

    def square():
        side = float(input("Side Length: "))
        area_square = side*side
        print(area_square)

    def rectangle():
        length = float(input("Length: "))
        breadth = float(input("Breadth: "))
        area_rectangle = length*breadth
        print(area_rectangle)

    def triangle():
        base = float(input("Base: "))
        height = float(input("Height: "))
        area_triangle = 1/2 * base * height
        print(area_triangle)

    def circle():
        radius = float(input("Radius: "))
        area_square = 3.14*radius*radius
        print(area_square)

    if choice == 1:
        square()

    elif choice == 2:
        rectangle()

    elif choice == 3:
        triangle()

    elif choice == 4:
        circle()