from string import ascii_lowercase
from api_reader import get_api_data as get_word


def print_welcome_message():
    print("""Welcome to my lovely Hangman project!
I hope you will enjoy the game!
""")


def ask_username():
    return input("What is your name?\n\n")


def get_abc_letters():
    return list(ascii_lowercase)


def create_string_from_unused_letters(unused_letters):
    printable_unused_letters = ""
    for letter in unused_letters:
        printable_unused_letters += letter + " "
    return printable_unused_letters[0:-1]


def print_unused_letters(unused_letters):
    print(f"Unused letters are: {create_string_from_unused_letters(unused_letters)}")


def print_covered_word(shown_letters):
    printable_word = ""
    for _ in shown_letters:
        printable_word += "_ "
    print(printable_word + "\n")
        

def ask_for_a_letter(unused_letters):
    print_unused_letters(unused_letters)
    current_letter = input("Please enter an unused letter!\n")
    return current_letter.lower()


def is_only_one_character(current_letter):
    return len(current_letter) == 1


def is_letter(current_letter):
    return current_letter.isalpha()


def is_unused(current_letter, unused_letters):
    return current_letter in unused_letters



def is_letter_valid(current_letter, unused_letters):
    return is_only_one_character(current_letter) and is_letter(current_letter) and is_unused(current_letter, unused_letters)


def main():
    test = ["a", "b"]
    unused_letters = get_abc_letters()
    print_welcome_message()
    username = ask_username()
    word = get_word()
    letters_to_check = list(word)
    shown_letters = list(word)
    print_covered_word(shown_letters)
    current_letter = ask_for_a_letter(unused_letters)
    
    
if __name__ == "__main__":
    main()