# Write a program that reads values from the user until a blank line is entered. Display the total of all of the
# values entered by the user (or 0.0 if the first value entered is a blank line). Complete this task using recursion.
# Your program may not use any loops.


total = 0.0
def total_values():

    # Call to function
    total_v()

    # Return numeric value
    return total


def total_v():

    # Request input from the user
    value = input("Please enter a value or enter to finish: ")
    global total

    # Check if it is a number
    if value.isdecimal():

        # Add the input value to total
        total += float(value)

        # Call recursive function
        total_values()

        # If input is blank return total value
    elif value == "":
        return total

    # If is not a number show message
    else:
        print("Input is not a valid number")
        total_values()


if __name__ == '__main__':
    print(f"Total of values {total_values()}")
