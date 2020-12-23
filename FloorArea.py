# Write a program that asks the user to enter the width and length of a room. Once
# the values have been read, your program should compute and display the area of the
# room. The length and the width will be entered as floating point numbers. Include
# units in your prompt and output message; either feet or meters, depending on which
# unit you are more comfortable working with

widht = float(input("Please enter the width of the room: "))
length = float(input("Please enter the length of the room: "))

print(f"The area of the room's floor is: {round(widht * length, 2)} meters")
#Comment additional

# D4 Challenge 1

def odd_even(num):
    return "The number entered is odd" if num % 2 != 0 else "The number entered is even"

num = int(input("Please enter a integer number: "))
print(odd_even(num))


# D4 Challenge 2
def vowel_consonant(str):
    if str == "a" or str == "e" or str == "i" or str == "o" or str == "u":
        print("The entered letter is a vowel")
    elif str == "y":
        print("Sometimes  is a vowel, and sometimes is a consonant")
    else:
        print("The entered letter is a consonant")

vowel_consonant(input("Please enter a letter"))



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

note=input("Please enter the note: ")

def get_frequency(note):
    str_note=list(note)
    octave_notes={"C4":261.63, "D4":293.66, "E4":329.63, "F4":349.23,"G4":392.00,
        "A4":440.00,"B4":493.88}
    freq=octave_notes.get(note) if note in octave_notes else 261.63
    print(f"note: {note}, freq: {freq}")
    if note in octave_notes:
        print(f"The frequency for the note {note} is: {freq}")
    elif "C" in note:
        frequency=freq/pow(2,4-int(str_note[1]))
        print(f"The frequency for the note {note} is: {frequency}")

get_frequency(note)

#License plate

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

#Roulette

from random import choice

def roulette():
    rou_dict={}
    for i in range(37):
        if i%2!=0 and i<10 or i%2==0 and i>10:
            rou_dict.update({str(i):"red"})
        elif i%2==0 and i<10 or i%2!=0 and i>10:
            rou_dict.update({str(i):"black"})
    rou_dict.update({"00":"green","0":"green"})
    selected=choice(list(rou_dict))
    select_int=int(selected)
    print(f"The spin resulted in {selected}...")
    if select_int>1:
        print("Pay Red") if rou_dict.get(selected)=="red" else print("Pay Black")
        print("Pay Even") if select_int%2==0 else print("Pay Odd")
        print("Pay 1 to 18") if select_int<19 else print("Pay 19 to 36")
    else:
        print(f"Pay {selected}")
roulette()