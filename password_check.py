# Option 2: Difficulty Level Pre-Intermediate:  In this exercise you will write
# a function that determines whether or not a password is good. We will define
# a good password to be a one that is at least 8 characters long and contains
# at least one uppercase letter, at least one lowercase letter, and at
# least one number. Your function should return true if the password passed
# to it as its only parameter is good. Otherwise it should return false.
# Include a main program that reads a password from the user and reports
# whether or not it is good
import re


def password_check(password):
    is_upper, is_lower, is_length = 0, 0, 0
    for char in password:
        if "A" <= char <= "Z": is_upper = +1
        if "a" <= char <= "z": is_lower = +1
    is_length = len(password) >= 8
    if is_length and is_lower and is_upper:
        print(f"The password {password} is good")
    else:
        print(f"The password {password} is not good")


if __name__ == '__main__':
    password_check(input("Please enter the pass word to be evaluated: "))
