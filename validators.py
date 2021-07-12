def is_between_zero_and_two(number_input):
    return 0 <= number_input < 3


def is_between_zero_and_three(number_input):
    return 0 <= number_input < 4


def is_only_number(number_input):
    return number_input.isdecimal()


def is_only_one_character(current_letter):
    return len(current_letter) == 1


def is_letter(current_letter):
    return current_letter.isalpha()


def is_unused(current_letter, used_letters):
    return current_letter in used_letters


def is_letter_valid(current_letter, unused_letters):
    return is_only_one_character(current_letter) and is_letter(current_letter) and is_unused(current_letter, unused_letters)


def is_letter_in_word(current_letter, letters_to_check):
    return current_letter in letters_to_check


def has_lives(lives):
    return 0 < lives


def guessed_word(shown_letters):
    return "_" not in shown_letters


def is_yes_or_no(input_string):
    return input_string.lower() == "yes" or input_string.lower() == "no"


def is_valid_difficulty(difficulty_input):
    difficulties = ["easy", "medium", "hard"]
    return difficulty_input in difficulties