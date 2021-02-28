# For this exercise I want you to write a function (calc) that expects a single argument -a string containing
# a simple math expression in prefix notation- with an operators and two numbers, your program will parse the input
# and will produce the appropriate output. For our purposes is enough to handle the six basic arithmetic operations
# in Python: addition, substraction, multiplication, division(/), modulus(%), and exponentiation(**). The normal Python
# math rules should work, such that division always result in a floating-point number.
# We will assume for our purposes that the argument will only contain one of our six operators and two valid numbers.
# But wait there is a catch -or a hint, if you prefer: you should implement each of the operations in a single function-
# and you shouldn't use an if statement to decide which function should be run. Another hint: look at the operator module
# whose functions implements many of the Python's operators

def calc(text):
    op, num1, num2 = text.split()
    oper = {"+": add, "-": sub, "*": mul, "/": div, "%": mod, "**": pow}
    first=int(num1)
    second=int(num2)
    return oper[op](first,second)

# Another option is just to reorder the expresion and evaluate it
def calc2(text):
    op, num1, num2 = text.split()
    return eval(num1+op+num2)


def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


def mod(num1, num2):
    return num1 % num2


def pow(num1, num2):
    return num1 ** num2


if __name__ == '__main__':
    print(calc("/ 10 5"))
    print(calc2("/ 10 5"))
