# Generate a strong password

from random import randint
from random import choice
import string


def generate_password() :
    # Use randint to select the length of the password between 12 and 15 chars
    nbr_of_chars = randint(12,15)
    # Init chars list that compose the password ("_""_"...)
    chars_list = []
    # Foreach char, choice to choose the kind of char which is also set with choice
    for i in range(nbr_of_chars) :
        method_used = choice(["lower_case", "upper_case", "digit", "punctuation", "special_char"])

        match method_used :
            case "lower_case":
                chars_list.append(choice(string.ascii_lowercase))
            case "upper_case":
                chars_list.append(choice(string.ascii_uppercase))
            case "digit":
                chars_list.append(choice(string.digits))
            case "punctuation":
                chars_list.append(choice(string.punctuation))
            case "special_char":
                chars_list.append(choice("&@#^$%+=µ"))

    # turn the list of chars into a string that is returned
    final_password = "".join(chars_list)
    return final_password


