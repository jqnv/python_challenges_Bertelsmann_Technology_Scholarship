# Option 2: Many people do not use capital letters correctly,
# especially when typing on small devices like smart phones. In this exercise,
# you will write a function that capitalizes the appropriate characters
# in a string. A lowercase “i” should be replaced with an uppercase “I”
# if it is both preceded and followed by a space....

import re


def capitalize():
    text = input("Please type the text to appropriate capitalize it: ")
    text = re.sub(" i ", " I ", text)
    text = re.sub("(^|[.?!])\s*([a-zA-Z])", lambda p: p.group(0).upper(), text)
    print(text)


capitalize()