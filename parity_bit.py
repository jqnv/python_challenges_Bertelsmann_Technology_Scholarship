# Option 2: Difficulty Level: Pre-Intermediate: A parity bit
# is a simple mechanism for detecting errors in data transmitted over
# an unreliable connection such as a telephone line. The basic idea is that
# an additional bit is transmitted after each group of 8 bits so that
# a single bit error in the transmission can be detected. Parity bits
# can be computed for either even parity or odd parity. If even parity is
# selected then the parity bit that is transmitted is chosen so that the
# total number of one bits transmitted (8 bits of data plus the parity bit)
# is even. When odd parity is selected the parity bit is chosen so that
# the total number of one bits transmitted is odd. Write a program that
# computes the parity bit for groups of 8 bits entered by the user using
# even parity. Your program should read strings containing 8 bits until
# the user enters a blank line. After each string is entered by the user
# your program should display a clear message indicating whether
# the parity bit should be 0 or 1. Display an appropriate error message
# if the user enters something other than 8 bits

def parity_bit():
    cost = 0
    while True:  # Loop continuously
        bits8 = input("Please enter 8 bits to transmit(each number may be either 1 or 0):")  # Get the input
        list_bits8=list(bits8)
        ones, zeros=list_bits8.count("1"), list_bits8.count("0")
        if bits8=="":break
        try:
            if int(bits8) !="int" and ones+zeros!=8:
                print("Wrong input. Only 8 numbers either 0s or 1s are allowed")
            else:
                print("The parity bit should be a 0") if ones % 2 == 0 else print("The parity bit should be a 1")
        except ValueError:
            print("Wrong input. Only 8 numbers either 0s or 1s are allowed")

parity_bit()