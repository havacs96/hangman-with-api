from string import ascii_lowercase

def print_welcome_message():
    print("""
Welcome to my lovely Hangman project!
I hope you will enjoy the game!
""")

def create_string_from_unused_letters(unused_letters):
    printable_unused_letters = ""
    for letter in unused_letters:
        printable_unused_letters += letter + " "
    return printable_unused_letters[0:-1]


def print_unused_letters(unused_letters):
    print(create_string_from_unused_letters(unused_letters))


def ask_username():
    return input("What is your name")


def ask_for_a_letter(unused_letters):
    print_unused_letters(unused_letters)
    return input("Please enter an unused letter!")


def get_abc_letters():
    return list(ascii_lowercase)

