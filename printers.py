from hangman import create_string_from_unused_letters


def print_welcome_message():
    print("""Welcome to my lovely Hangman project!
I hope you will enjoy the game!
""")


def print_menu_message():
    print("""Welcome to the game menu! Please enter a number!
Write "1" for playing Hangman,
write "2" for seeing the statistics menu,
write "0" to exit from the program!
""")


def print_difficulty_message():
    print("""Please enter a number!
Write "1" for easy difficulty,
write "2" for medium difficulty,
write "3" for hard difficulty,
write "0" to go back to the game menu!
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