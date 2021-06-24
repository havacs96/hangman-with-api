from string import ascii_lowercase
from api_reader import get_api_data as get_word
import printers

SPECIAL_CHARACTERS = [".", "'", " ", "-", "?", "!"]

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


def is_only_one_character(current_letter):
    return len(current_letter) == 1


def is_letter(current_letter):
    return current_letter.isalpha()


def is_unused(current_letter, used_letters):
    return current_letter in used_letters



def is_letter_valid(current_letter, unused_letters):
    return is_only_one_character(current_letter) and is_letter(current_letter) and is_unused(current_letter, unused_letters)


def get_valid_letter(unused_letters):
    while True:
        current_letter = ask_for_a_letter(unused_letters)
        if is_letter_valid(current_letter, unused_letters):
            return current_letter
        print("Invalid letter input! Please try again!")


def remove_used_letter(current_letter, unused_letters):
    unused_letters.remove(current_letter)


def is_letter_in_word(current_letter, letters_to_check):
    return current_letter in letters_to_check


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
    

def has_lives(lives):
    return 0 < lives


def guessed_word(shown_letters):
    return "_" not in shown_letters


def main():
    lives = 6
    is_over = False
    unused_letters = get_abc_letters()
    printers.print_welcome_message()
    username = ask_username()
    word = get_word()
    letters_to_check = list(word)
    shown_letters = ["_" if x not in SPECIAL_CHARACTERS else x for x in letters_to_check]
    while not is_over:
        printers.print_covered_word(shown_letters)
        current_letter = get_valid_letter(unused_letters)
        remove_used_letter(current_letter, unused_letters)
        if is_letter_in_word(current_letter, letters_to_check):
            replace_correct_guesses(current_letter, letters_to_check, shown_letters)
        else:
            lives -= 1
        if not has_lives(lives):
            is_over = True
            printers.print_lose_message()
        if guessed_word(shown_letters):
            is_over = True
            printers.print_winning_message()

    
if __name__ == "__main__":
    main()