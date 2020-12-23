#Option 1 Difficulty Level: Elementary: A triangle can be classified
# based on the lengths of its sides as equilateral, isosceles or scalene.
# All 3 sides of an equilateral triangle have the same length. An isosceles
#triangle has two sides that are the same length, and a third side
# that is a different length. If all of the sides have different lengths
# then the triangle is scalene. Write a program that reads the lengths of 3 sides
# of a triangle from the user. Display a message indicating the type of the triangle.

side1=float(input("Please enter the length of the first side of the triangle"))
side2=float(input("Please enter the length of the second side of the triangle"))
side3=float(input("Please enter the length of the third side of the triangle"))
def triangle_classify(side1, side2,side3):
    if side1==side2 and side2==side3:
        print("This is an equilateral triangle")
    elif side1==side2 or side2==side3 or side1==side3:
        print("This is an isosceles triangle")
    else:
        print("This is an scalene triangle")

triangle_classify(side1,side2,side3)