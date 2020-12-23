#License plate
#Option 1 Difficulty Level: Elementary: In a particular jurisdiction,
# older license plates consist of three uppercase letters followed by three numbers.
# When all of the license plates following that pattern had been used, the format was
# changed to four numbers followed by three uppercase
#letters. Write a program that begins by reading a string of characters from the user.
# Then your program should display a message indicating whether the characters
# are valid for an older style license plate or a newer style license plate.
# Your program should display an appropriate message if the string entered by the user
# is not valid for either style of license plate.

def valid_plate():
    plate_input=input("Please enter the license plate: ")
    if len(plate_input)==6:
        letters, numbers=plate_input[:3], plate_input[3:]
        valid_style(letters, numbers, plate_input)
    elif len(plate_input)==7:
        numbers, letters = plate_input[:4], plate_input[4:]
        valid_style(letters, numbers, plate_input)
    else:
        print(f"The plate {plate_input} is not a valid stYle for a license plate")

def valid_style(letters, numbers, plate_input):
    if letters.isupper() and numbers.isdigit():
        print(f"Plate {plate_input} is an valid style of plate")
    else:
        print(f"The plate {plate_input} is not a valid stYle for a license plate")

valid_plate()