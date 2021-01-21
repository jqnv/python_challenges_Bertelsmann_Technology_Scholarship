# Create a program that sums all of the numbers entered by the user while ignoring any lines entered by the user that
# are not valid numbers. Your program should display the current sum after each number is entered. It should display an
# appropriate error message after any invalid input, and then continue to sum any additional numbers entered by the user.
# Your program should exit when the user enters a blank # line. Ensure that your program works correctly for both
# integers and floating point numbers


def sum_numbers():
    total = 0
    # Loop to request numbers from the user multiple times
    while True:

        # Catch errors if not valid values are entered
        try:
            num = input("Please enter a number to get the total:")  # Get the input
            # Finish the program if blank is entered
            if num == "":
                break

            # Increase the variable total adding the number entered
            total += float(num)

        # Print error message if a valid number number is not entered
        except ValueError:
            print(f"The value entered '{num}' is not a valid number")

        # Print the total value
        finally:
            print(f"The total is {total}")


if __name__ == '__main__':
    sum_numbers()
