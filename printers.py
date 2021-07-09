from hangman import create_string_from_unused_letters


def print_welcome_message():
    print("""Welcome to my lovely Hangman project!
I hope you will enjoy the game!
""")


def print_menu_message():
    print("""Welcome to the game menu!
Write "1" for playing Hangman,
write "2" for seeing the statistics menu,
write "0" to exit from the program!
""")


def print_difficulty_message():
    print("""Write "1" for easy difficulty (word length is between 14 and 25),
write "2" for medium difficulty (word length is between 8 and 14),
write "3" for hard difficulty (word length is between 3 and 8),
write "0" to go back to the game menu!
BE VERY CAREFUL! Even the easy difficulty can be hard!
""")


def print_unused_letters(unused_letters):
    print(f"Unused letters are: {create_string_from_unused_letters(unused_letters)}")


def print_covered_word(shown_letters):
    printable_word = ""
    for element in shown_letters:
        printable_word += f"{element} "
    print(printable_word + "\n")


def print_lives_left(lives):
    if 1 < lives:
        print(f'You have {lives} lives left.')
    else:
        print(f'You have {lives} life left.')


def print_winning_message(word, user_name):
    print(f"Congratulations {user_name}! You won!")
    print_correct_word(word)


def print_lose_message(word):
    print("Unfortunatelly you lost! Do not give up!")
    print_correct_word(word)


def print_correct_word(word):
    print(f'The correct word was {word}!\n')


def print_score(score):
    print(f"Your score is {score}!")


def print_play_again_message(user_name):
    print(f"{user_name}, would you like to go to the menu?")
    print('Type "yes" if you want to and type "no" if you do not!')