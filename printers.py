from hangman import create_string_from_unused_letters


def print_welcome_message():
    print("""Welcome to my lovely Hangman project!
I hope you will enjoy the game!
""")


def print_unused_letters(unused_letters):
    print(f"Unused letters are: {create_string_from_unused_letters(unused_letters)}")


def print_covered_word(shown_letters):
    printable_word = ""
    for element in shown_letters:
        printable_word += f"{element} "
    print(printable_word + "\n")


def print_winning_message():
    print("Congratulations! You won!")


def print_lose_message():
    print("Unfortunatelly you lost! Do not give up!")
