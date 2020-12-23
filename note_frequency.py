
#Option 2: Difficulty Level: Pre-Intermediate: Begin by writing a program
# that reads the name of a note from the user and displays the note’s frequency.
# Your program should support all of the notes listed previously.
# (please see the attached image for more detail)

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
