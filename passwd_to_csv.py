# For this exercise, create a function, passwd_to_csv, that takes two filenames as arguments: the first is a
# passwd-style file to read from, and the second is the name of a file in which to write the output.The new file’s
# contents are the username (index 0) and the user ID (index 2).Note that a record may contain a comment,
# in which case it will not have anything at index 2; you should take that into consideration when writing
# the file.The output file should use TAB characters to separate the elements.

# To run the file at the command line Prompt>python passwd_to_csv.py in_file.csv out_file.csv
import csv
from sys import argv


# Function to read username and userID from a csv file
# Creating a new csv file with just the info required
def passwd_to_csv():

    # Get the name of input and output files
    f_in=argv[1]
    f_out=argv[2]

    # Read input file line by line storing every element in the data list
    with open(f_in, mode="r") as f_input:
        for line in f_input:
            data = line.split(":")
            text=line.strip()

            # Ignoring any line without a colon separating strings
            if len(text)>2 and text.find(":")!=-1:

                # Writing username and userID to a new file separated by a tab character
                with open(f_out,mode="a",newline='') as f_output:
                    o=csv.writer(f_output)
                    o.writerow([data[0],"\t",data[2]])


if __name__ == '__main__':
    passwd_to_csv()
