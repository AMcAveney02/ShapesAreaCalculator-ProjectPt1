import math

def area_of_circle(radius) -> float:
    """
    Function to compute the area of a circle
    :param radius: First inputed value
    :return: Product of (pi * radius**2)
    """
    if type(radius) == str: # checks to make sure radius input is not a string, if it is raises a type error
        raise TypeError
    if radius < 0: # checks to make sure radius input is not negative, if it is raises a value error
        raise ValueError
    else: # if input is not negative or a string, the function will execute and return the answer
        a = float(math.pi * math.pow(radius, 2))
        return a

def area_of_rectangle(length, width) -> float:
    """
    Function to compute the area of a rectangle
    :param length: First inputed value for the length of the side of a rectangle
    :param width: Second inputed value for the width of the side of a rectangle
    :return: Product of (length * width)
    """
    if type(length) != int and type(length) != float and type(width) != int and type(width) != float:
        raise TypeError # checks to make sure input for length and width is not a string
    if length < 0: # raises a value error if length input is a negative
        raise ValueError
    if width < 0: # raises a value error if the width input is a negative
        raise ValueError
    else: # if the input for both length and width is valid it will execute the function and return the answer
        a = float(length * width)
        return a

def area_of_square(square_length) -> float:
    """
    Function to compute the area of a square
    :param square_length: First inputed value for the length of the sides of the square
    :return: Product of (square_length * square_length)
    """
    if type(square_length) == str: # raises a type error if the input is a string
        raise TypeError
    if square_length < 0: # checks to make sure input is not negative
        raise ValueError
    else: # if the input is valid it will execute the function and return the answer
        a = float(square_length * square_length)
        return a

def area_of_triangle(base, height) -> float:
    """
    Function to compute the area of a triangle
    :param base: First inputed value for the base of the triangle
    :param height: Second inputed value for the height of the triagle
    :return: Product of (1/2 * (base * height))
    """
    if type(base) != int and type(base) != float and type(height) != int and type(height) != float:
        raise TypeError # checks for string input in base and height and raises a type error
    if base < 0:
        raise ValueError # checks for negative input for base and raises a value error
    if height < 0:
        raise ValueError # checks for negative input for height and raises a value error
    else: # if the input is valid the function will execute the following formula
        a = float(0.5 * (base * height))
        return a

def power_of_number(number_base, exponent) -> float:
    """
    Function to compute raisign a number to a power
    :param number_base: First inputed value for the base number of the power function
    :param exponent: Second inputed value for the exponent of the power function
    :return: Product of (base ** exponent)
    """
    if type(number_base) != int and type(number_base) != float and type(exponent) != int and type(exponent) != float:
        raise TypeError # checks to make sure that number_base and exponent are not a string
    else: # executes the function and completes the formula if the inputs are valid (i.e. not strings)
        a = float(math.pow(number_base, exponent))
        return a






