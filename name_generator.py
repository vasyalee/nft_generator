from secrets import *
import string


def generate_name():
    endings = ["ur", "hvar", "bruh", "urmur", "bar"]
    alphabet_lowercase = string.ascii_lowercase
    alphabet_uppercase = string.ascii_uppercase


    creature_name = ''

    for k in range(5):
        creature_name += choice(alphabet_lowercase)

    creature_name = choice(alphabet_uppercase) + creature_name + choice(endings)
    return creature_name


