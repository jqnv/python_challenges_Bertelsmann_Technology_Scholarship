# Write a function that takes two positive integers that represent
# the numerator and denominator of a fraction as its only two parameters.
# The body of the function should reduce the fraction to lowest terms and
# then return both the numerator and denominator of the reduced fraction as
# its result. For example, if the parameters passed to the function are 6 and 63
# then the function should return 2 and 21. Include a main program that allows
# the user to enter a numerator and denominator. Then your program should display
# the reduced fraction.

def reduce_fraction(num, den):
    num_p, den_p = num, den
    for i in range(2, max(num, den) + 1):
        if num % i == 0 and den % i == 0:
            num /= i
            den /= i
    print(f"The reduced fraction of {num_p}/{den_p} is {int(num)}/{int(den)}")


num = int(input("Please enter the numerator of the fraction to reduce: "))
den = int(input("Please enter the denominator of the fraction to reduce: "))
reduce_fraction(num, den)
