# Option 1 Difficulty Level: Elementary: One of the first known
# examples of encryption was used by Julius Caesar. Caesar needed
# to provide written instructions to his generals, but he didn’t want
# his enemies to learn his plans if the message slipped into their hands.
# As result, he developed what later became known as the Caesar Cipher.
# The idea behind this cipher is simple (and as a result, it provides
# no protection against modern code breaking techniques). Each letter in the
# original # message is shifted by 3 places. As a result, A becomes D,
# B becomes E, C becomes F, D becomes G, etc. The last three letters in the alphabet
# are wrapped around to the beginning: X becomes A, Y becomes B and Z becomes C.
# Non-letter characters are not modified by the cipher. Write a program that
# implements a Caesar cipher. Allow the user to supply the message and the
# shift amount, and then display the shifted message. Ensure that your program
# encodes both uppercase and lowercase letters. Your program should also support
# negative shift values so that it can be used both to encode messages and decode
# messages. (please see the attached image for more detail)
import string
from itertools import chain


def caesar_cipher():
    message = input("Please enter the message to code: ")
    shift = int(input("Please enter the shift to code: "))
    alpha_low = list(string.ascii_lowercase)
    alpha_upp = list(string.ascii_uppercase)
    alpha_low.extend(alpha_upp)
    if shift >= 0:
        low_a, low_z, upp_a, upp_z = ord("a") + shift, ord("z") + 1, ord("A") + shift, ord("Z") + 1
        code_low = list(chain(range(low_a, low_z), range(ord("a"), low_a)))
        code_upp = list(chain(range(upp_a, upp_z), range(ord("A"), upp_a)))
    else:
        low_a, low_z, upp_a, upp_z = ord("a"), ord("z") + shift + 1, ord("A"), ord("Z") + shift + 1
        code_low = list(chain(range(low_z, ord("z") + 1), range(low_a, low_z)))
        code_upp = list(chain(range(upp_z, ord("Z") + 1), range(upp_a, upp_z)))
        print(code_low)
    code_low.extend(code_upp)
    code_iter = dict(zip(alpha_low, code_low))
    print(code_iter)
    coded_list = []
    for i in message:
        if ("a" <= i <= "z") or ("A" <= i <= "Z"):
            coded_list.append(chr(code_iter.get(i)))
        else:
            coded_list.append(i)
    coded_message = ''.join(coded_list)
    print(coded_message)


caesar_cipher()