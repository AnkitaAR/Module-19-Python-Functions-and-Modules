def perimeter_of_rectangle(length, width):
    """
    Calculate the perimeter of a rectangle.

    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    float: The perimeter of the rectangle.
    """
    return 2 * (length + width)
def perimeter_of_circle(radius):
    """
    Calculate the perimeter (circumference) of a circle.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The perimeter of the circle.
    """
    import math
    return 2 * math.pi * radius
def perimeter_of_triangle(side1, side2, side3):
    """

    Calculate the perimeter of a triangle.
    Parameters:
    side1 (float): The length of the first side of the triangle.
    side2 (float): The length of the second side of the triangle.
    side3 (float): The length of the third side of the triangle.

    Returns:
    float: The perimeter of the triangle.
    """
    return side1 + side2 + side3
def perimeter_of_square(side):
    """
    Calculate the perimeter of a square
    Parameters:
    side (float): The length of one side of the square.

    Returns:
    float: The perimeter of the square.
    """
    return 4 * side
r=input("Enter the radius of the circle:")
print("Perimeter of the circle is:",perimeter_of_circle(float(r)))
l=input("Enter the length of the rectangle:")
w=input("Enter the width of the rectangle:")
print("Perimeter of the rectangle is:",perimeter_of_rectangle(float(l),float(w)))
s1=input("Enter the length of the first side of the triangle:")
s2=input("Enter the length of the second side of the triangle:")
s3=input("Enter the length of the third side of the triangle:")
print("Perimeter of the triangle is:",perimeter_of_triangle(float(s1),float(s2),float(s3)))
side=input("Enter the length of one side of the square:")
print("Perimeter of the square is:",perimeter_of_square(float(side)))