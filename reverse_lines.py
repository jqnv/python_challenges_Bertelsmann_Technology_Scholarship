# In this function, we do a basic version of this idea. The function takes two arguments: the names of the input
# file (to be read from) and the output file (which will be created).


def reverse_lines(orig_f, targ_f):
    # Read original file storing one line at the time
    with open(orig_f, mode="r") as f_input:
        for line in f_input:
            # Reverse the line and adding new line at the end
            line = line.rstrip()[::-1] + "\n"

            # Write every reversed line to a new target file
            with open(targ_f, mode="a") as f_output:
                f_output.write(line)


if __name__ == '__main__':
    # Declaring the names of the files to be send as parameters in the function
    orig_file = "orig_f.txt"
    targ_file = "targ_f.txt"
    reverse_lines(orig_file, targ_file)
