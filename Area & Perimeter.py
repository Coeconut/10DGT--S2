# Finding the Area & Perimeter of a circle or rectangle
# Author: Andrew Coe
# Date: 2024-10-30
# Ver: 5.0

import math

def print_line():
    print("-" * 50)

def measurement():
    while True:
        print("\nWelcome to the Area and Perimeter Calculator")
        print_line()
        
        while True:
            try:
                shape = int(input("Is the shape a Circle (1) or Rectangle (2):\n"))
                if shape in [1, 2]:
                    break
                else:
                    print("Error! Enter 1 for Circle or 2 for Rectangle.\n")
            except ValueError:
                print("ValueError, Enter a number 1 or 2\n")

        while True:
            try:
                units_num = int(input("\nWhat units of measurements are you using\nMeters(1), Centimeters(2), Feet(3) or Inches(4):\n"))
                if units_num in [1, 2, 3, 4]:
                    break
                else:
                    print("Error enter a number 1-4\n")
            except ValueError:
                print("ValueError, Enter a number 1-4\n")

        units_dict = {1: "Meters", 2: "Centimeters", 3: "Feet", 4: "Inches"}
        units = units_dict[units_num]

        if shape == 1:
            while True:
                try:
                    radius = float(input("\nWhat is the radius of the Circle: \n"))
                    if radius > 0:
                        break
                    else:
                        print("Error, radius must be a positive number")
                except ValueError:
                    print("Error, this is not algebra, enter a number")
            
            area = math.pi * (radius ** 2)
            perimeter = 2 * math.pi * radius

            print("\nResults for Circle")
            print_line()
            print(f"Area: {area:.2f} {units} squared")
            print(f"Perimeter: {perimeter:.2f} {units}")

        elif shape == 2:
            while True:
                try:
                    width = float(input("\nWhat is the width of the Rectangle: \n"))
                    if width > 0:
                        break
                    else:
                        print("Error, width must be a positive number")
                except ValueError:
                    print("Error, this is not algebra, enter a number")

            while True:
                try:
                    height = float(input("\nWhat is the height of the Rectangle: \n"))
                    if height > 0:
                        break
                    else:
                        print("Error, height must be a positive number")
                except ValueError:
                    print("Error, this is not algebra, enter a number")

            area = width * height
            perimeter = 2 * (width + height)

            print("\nResults for Rectangle")
            print_line()
            print(f"Area: {area:.2f} {units} squared")
            print(f"Perimeter: {perimeter:.2f} {units}")

        again = input("\nPress Enter to do it again or any other key to exit: ")
        if again != "":
            break

measurement()
