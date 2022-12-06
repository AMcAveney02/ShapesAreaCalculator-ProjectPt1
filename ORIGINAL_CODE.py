# Part 1
# Import the necessary modules
# This is all the original code from lab 3 from which I built the project off of.
from shapes import area, perimeter

def selection():
    print('----------------------')
    print('SELECT SHAPE')
    print('----------------------')
    print('1 - Circle')
    print('2 - Rectangle')
    print('3 - Square')
    print('4 - Triangle')

    # Code to check that a valid shape has been selected
    shape = int(input('Shape number: '))
    while shape < 1 or shape > 4:
        shape = int(input('Shape number (1-4): '))
    return shape

def main():
    while True:
        shape = selection()

        computation = int(input('Computation (Area = 1 or Perimeter = 2): '))
        while computation < 1 or computation > 2:
            computation = int(input('Enter 1 or 2: '))

        if shape == 1 and computation == 1:
            radius = float(input("Circle radius: "))
            circle_area = area.a_circle(radius)
            print(f"Circle area = {circle_area:.2f}")
        elif shape == 1 and computation == 2:
            radius = float(input("Circle radius: "))
            circle_perimeter = perimeter.p_circle(radius)
            print(f"Circle perimeter = {circle_perimeter:.2f}")
        elif shape == 2 and computation == 1:
            length = float(input("Rectangle length: "))
            width = float(input("Rectangle width: "))
            rectangle_area = area.a_rectangle(length, width)
            print(f"Rectangle area = {rectangle_area:.2f}")
        elif shape == 2 and computation == 2:
            length = float(input("Rectangle length: "))
            width = float(input("Rectangle width: "))
            rectangle_perimeter = perimeter.p_rectangle(length, width)
            print(f"Rectangle perimeter = {rectangle_perimeter:.2f}")
        elif shape == 3 and computation == 1:
            square_length = float(input("Square length: "))
            square_area = area.a_square(square_length)
            print(f"Square area = {square_area:.2f}")
        elif shape == 3 and computation == 2:
            square_length = float(input("Square length: "))
            square_perimeter = perimeter.p_square(square_length)
            print(f"Square area = {square_perimeter:.2f}")
        elif shape == 4 and computation == 1:
            side_1 = float(input("Triangle side 1: "))
            side_2 = float(input("Triangle side 2: "))
            triangle_area = area.a_triangle(side_1, side_2)
            print(f"Triangle area = {triangle_area:.2f}")
        elif shape == 4 and computation == 2:
            side_1 = float(input("Triangle side 1: "))
            side_2 = float(input("Triangle side 2: "))
            side_3 = float(input("Triangle side 3: "))
            triangle_permimeter = perimeter.p_triangle(side_1, side_2, side_3)
            print(f"Triangle area = {triangle_permimeter:.2f}")

        loop_continue = input("Continue (y-n)" ).strip().lower()
        while loop_continue != "y" and loop_continue != "n":
            loop_continue = input("Enter y or n: ").strip().lower()
        if loop_continue == "y":
            continue
        if loop_continue == "n":
            print("PROGRAM DONE")
            break


if __name__ == '__main__':
    main()