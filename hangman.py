def print_welcome_message():
    print("""
Welcome to my lovely Hangman project!
I hope you will enjoy the game!
""")

#Unused letters is only a string
def print_unused_letters(unused_letters):
    print(unused_letters)


def ask_username():
    return input("What is your name")


def ask_for_a_letter(unused_letters):
    print_unused_letters(unused_letters)
    letter = input("Please enter an unused letter!")
    return letter







