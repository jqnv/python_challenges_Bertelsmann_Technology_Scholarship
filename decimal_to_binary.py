# Option 1 Difficulty Level: Elementary: Write a program that converts
# a decimal (base 10) number to binary (base 2). Read the decimal number from
# the user as an integer and then use the division algorithm shown below to
# perform the conversion. When the algorithm completes, result contains the
# binary representation of the number. Display the result, along with an
# appropriate message....
import math

def decimal_to_binary():
    q=input("Please enter the decimal number to convert to binary: ")
    q_int=int(q)
    result=""
    while True:
        r=q_int%2
        result=result+str(r)
        q_int=math.floor(q_int/2)
        if q_int==0:
            print(f"Decial number {q} converted to binary is {result}")
            break

decimal_to_binary()