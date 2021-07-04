from hangman import create_string_from_unused_letters


def print_welcome_message():
    print("""Welcome to my lovely Hangman project!
I hope you will enjoy the game!
""")


def print_menu_message():
    print("""Welcome to the game menu! Please enter a number!
Write "1" for playing Hangman,
write "2" for seeing the statistics menu,
write "0" to exit from the program
""")


def print_unused_letters(unused_letters):
    print(f"Unused letters are: {create_string_from_unused_letters(unused_letters)}")


def print_covered_word(shown_letters):
    printable_word = ""
    for element in shown_letters:
        printable_word += f"{element} "
    print(printable_word + "\n")


def print_winning_message(word):
    print("Congratulations! You won!")
    print_correct_word(word)



def print_lose_message(word):
    print("Unfortunatelly you lost! Do not give up!")
    print_correct_word(word)



def print_correct_word(word):
    print(f'The correct word was {word}!')


def print_score(score):
    print(f"Your score is {score}!")