#Option 1 Difficulty Level: Elementary: Write a program that reads
# an integer from the user. Then your program should display a message
# indicating whether the integer is even or odd.

def odd_even(num):
    return "The number entered is odd" if num % 2 != 0 else "The number entered is even"

num = int(input("Please enter a integer number: "))
print(odd_even(num))