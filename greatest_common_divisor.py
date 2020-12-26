# Option 2: Difficulty Level: Pre-Intermediate:  The greatest common divisor
# of two positive integers, n and m, is the largest number,
# d, which divides evenly into both n and m. There are several algorithms
# that can be used to solve this problem, including: Initialize d to the
# smaller of m and n

def greatest_common_divisor():
    n = int(input("Please enter the first number to get the GCD: "))
    m = int(input("Please enter the second number to get the GCD: "))
    d = 24
    while m % d != 0 or n % d != 0:
        d -= 1
    print(f"The greatest common divisor of {n} and {m} is {d}")


greatest_common_divisor()