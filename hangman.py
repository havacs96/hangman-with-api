from string import ascii_lowercase
from api_reader import get_api_data as get_word
import printers
import validators
import os
import sys

SPECIAL_CHARACTERS = [".", "'", " ", "-", "?", "!"]


def ask_for_menu_action():
    printers.print_menu_message()
    while True:
        menu_action = input("Please enter a number between!\n")
        if validators.is_only_number(menu_action) and validators.is_between_zero_and_two(int(menu_action)):
            return int(menu_action)
        print(f"{menu_action} is an invalid input!")


def ask_username():
    return input("What is your name?\n\n")


def get_abc_letters():
    return list(ascii_lowercase)


def create_string_from_unused_letters(unused_letters):
    printable_unused_letters = ""
    for letter in unused_letters:
        printable_unused_letters += letter + " "
    return printable_unused_letters[0:-1]
        

def ask_for_a_letter(unused_letters):
    printers.print_unused_letters(unused_letters)
    current_letter = input("Please enter an unused letter!\n")
    return current_letter.lower()


def get_valid_letter(unused_letters):
    while True:
        current_letter = ask_for_a_letter(unused_letters)
        if validators.is_letter_valid(current_letter, unused_letters):
            return current_letter
        print("Invalid letter input! Please try again!")


def remove_used_letter(current_letter, unused_letters):
    unused_letters.remove(current_letter)


def get_letter_indicies(current_letter, letters_to_check):
    letters_indicies = []
    index = 0
    for letter in letters_to_check:
        if current_letter == letter:
            letters_indicies.append(index)
        index += 1
    return letters_indicies


def replace_correct_guesses(current_letter, letters_to_check, shown_letters):
    letter_indicies = get_letter_indicies(current_letter, letters_to_check)
    for position in letter_indicies:
        shown_letters[position] = current_letter


def guess_the_word(is_over, lives, shown_letters, unused_letters, letters_to_check, word, score):
    while not is_over:
        os.system('cls||clear')
        printers.print_lives_left(lives)
        printers.print_covered_word(shown_letters)
        current_letter = get_valid_letter(unused_letters)
        remove_used_letter(current_letter, unused_letters)
        if validators.is_letter_in_word(current_letter, letters_to_check):
            replace_correct_guesses(current_letter, letters_to_check, shown_letters)
        else:
            lives -= 1
        if not validators.has_lives(lives):
            is_over = True
            printers.print_lose_message(word)
        if validators.guessed_word(shown_letters):
            is_over = True
            score += 2
            printers.print_score(score)
            printers.print_winning_message(word)


def play_hangman():
    lives = 6
    score = 0
    is_over = False
    printers.print_welcome_message()
    unused_letters = get_abc_letters()
    username = ask_username()
    word = get_word()
    letters_to_check = list(word)
    shown_letters = ["_" if x not in SPECIAL_CHARACTERS else x for x in letters_to_check]
    guess_the_word(is_over, lives, shown_letters, unused_letters, letters_to_check, word, score)


def make_action_by_menu_input():
    menu_input = ask_for_menu_action()
    if menu_input == 1:
        play_hangman()
    elif menu_input == 2:
        #show statistics
        pass
    elif menu_input == 0:
        #quit
        sys.exit(0)


def main():
    make_action_by_menu_input()
        

    
if __name__ == "__main__":
    main()