# In this exercise, write a function, passwd_to_dict, that reads from a Unix-style “password file,”
# commonly stored as/etc/passwd, and returns a dict based on it. Each line is one user record, divided into
# colon-separated fields.The first field (index 0) is the username, and the third field(index 2) is the user’s
# unique ID number.(In the system from which I took the /etc/passwd file, nobody has ID -2, root has ID 0, and daemon
# has ID 1.) For our purposes, you can ignore all but these two fields.Sometimes, the file will contain lines that
# fail to adhere to this format. For example, we generally ignore lines containing nothing but whitespace.
# Some vendors (e.g., Apple) include comments in their/etc/passwd files, in which the line starts with a #character.
# The function passwd_to_dict should return a dict based on/etc/passwd in which the dict’s keys are usernames
# and the values are the users’ IDs.

def passwd_to_dict():
    my_dict = {}
    # Open the file using and alias
    with open("passwd.txt") as my_file:
        # Print the content of last 10 lines using deque
        for line in my_file:
            if line.startswith("#") == False and line.strip() != "":
                text = line.split(":")
                my_dict.update({text[0]: text[2]})
        return (my_dict)


if __name__ == '__main__':
    print(passwd_to_dict())
