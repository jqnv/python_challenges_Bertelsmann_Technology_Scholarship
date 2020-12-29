# Option 1 Difficulty Level: Elementary: Write a function that generates a
# random password. The password should have a random length of between 7 and 10
# characters. Each character should be randomly selected
# from positions 33 to 126 in the ASCII table. Your function will not take
# any parameters. It will return the randomly generated password as its only
# result. Display the randomly generated password in your file’s main program.
# Your main program should only run when your solution has not been imported
# into another file
from random import randint


def rand_password():
    num_char = randint(7, 10)
    char_p = []
    for i in range(num_char):
        char_p.append(chr(randint(33, 126)))
    print(f"The random generated {num_char} charactes password is {''.join(char_p)}")


if __name__ == '__main__':
    rand_password()
