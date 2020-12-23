# Option 2: Difficulty Level: Pre-Intermediate: In this exercise
# you will create a program that reads a letter of the alphabet from the user.
# If the user enters a, e, i, o or u then your program should display a message
# indicating that the entered letter is a vowel. If the user enters y
# then your program should display a message indicating that sometimes y is a vowel,
# and sometimes y is a consonant. Otherwise your program should display a message
# indicating that the letter is a consonant.

def vowel_consonant(str):
    if str == "a" or str == "e" or str == "i" or str == "o" or str == "u":
        print("The entered letter is a vowel")
    elif str == "y":
        print("Sometimes  is a vowel, and sometimes is a consonant")
    else:
        print("The entered letter is a consonant")


vowel_consonant(input("Please enter a letter"))
