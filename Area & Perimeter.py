# Finding the Area & Perimeter of a circle or rectangle
# Author: Andrew Coe
# Date: 2024-10-30
# Ver: 5.0


# Importing Math
import math


# Creates a function(Reuseable code) called measurement
def measurement():
    while True:
        # Prints Wecome message
        print("\nWelcome to the Area and Perimeter Calculator")
        print("--------------------------------------------------")
        
        while True:
            try:
                # Ask if the user what the Area and Perimeter of a Circle or a Rectangle
                shape = int(input("Is the shape a Circle (1) or Rectangle (2):\n"))
                # See's if the number is valid shape
                if shape in [1, 2]:
                    break
                # Error for a integer that is not 1 or 2
                else:
                    print("Error! Enter 1 for Circle or 2 for Rectangle.\n")
            # Error for any response that isn't it integer
            except ValueError:
                print("ValueError!, Enter 1 for Circle or 2 for Rectangle.\n")

        while True:
            try:
                # Ask if the user what unit of measurement they want to use 
                units_num = int(input("\nWhat units of measurements are you using\nMeters(1), Centimeters(2), Feet(3) or Inches(4):\n"))
                # See's if the number is valid unit of measurement
                if units_num in [1, 2, 3, 4]:
                    break
                # Error for a integer that is not 1,2,3 or 4
                else:
                    print("Error enter a number 1-4\n")
            # Error for any response that isn't it integer
            except ValueError:
                print("ValueError, Enter a number 1-4\n")
        # Changes the numbers into units of measurement
        units_dict = {1: "Meters", 2: "Centimeters", 3: "Feet", 4: "Inches"}
        units = units_dict[units_num]

        # See's if the shape is a circle
        if shape == 1:
            while True:
                try:
                    # Asks for the radius of the Circle
                    radius = float(input("\nWhat is the radius of the Circle: \n"))
                    # If raduis is more then 0 then it is vilid
                    if radius > 0:
                        break
                    # If raduis is 0 or less it prints a Error
                    else:
                        print("Error, radius must be a positive number")
                # If raduis is not a number it prints a Error
                except ValueError:
                    print("Error, this is not algebra, enter a number")
            
            # Calulates the Area and Perimeter of the Circle
            area = math.pi * (radius ** 2)
            perimeter = 2 * math.pi * radius

            # Prints out the Reults of the Area and Perimeter
            print("\nResults for Circle")
            print("--------------------------------------------------")
            print(f"Area: {area:.2f} {units} squared")
            print(f"Perimeter: {perimeter:.2f} {units}")

        # See's if the shape is a Rectangle
        elif shape == 2:
            while True:
                try:
                    # Asks for the width of the Rectangle
                    width = float(input("\nWhat is the width of the Rectangle: \n"))
                    # If width is more then 0 then it is vilid
                    if width > 0:
                        break
                    # If width is 0 or less it prints a Error
                    else:
                        print("Error, width must be a positive number")
                # If width is not a number it prints a Error
                except ValueError:
                    print("Error, this is not algebra, enter a number")

            while True:
                try:
                    # Asks for the height of the Rectangle
                    height = float(input("\nWhat is the height of the Rectangle: \n"))
                    # If height is more then 0 then it is vilid
                    if height > 0:
                        break
                    # If height is 0 or less it prints a Error
                    else:
                        print("Error, height must be a positive number")
                # If height is not a number it prints a Error
                except ValueError:
                    print("Error, this is not algebra, enter a number")

            # Calulates the Area and Perimeter of the Rectangle
            area = width * height
            perimeter = 2 * (width + height)

            # Prints out the Reults of the Area and Perimeter
            print("\nResults for Rectangle")
            print("--------------------------------------------------")
            print(f"Area: {area:.2f} {units} squared")
            print(f"Perimeter: {perimeter:.2f} {units}")

        # Asks if The user wants the Area and Perimeter of another shape
        again = input("\nPress Enter to do it again or any other key to exit: ")
        if again != "":
            break

# activate the function
measurement()
