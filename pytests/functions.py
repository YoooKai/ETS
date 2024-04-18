def sum_nums(num1, num2):
    return num1 + num2


def a_greater_than(num1, num2):
    return num1 > num2


def is_pangram(text):
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    text_uniquechars = set(text.lower())
    for char in text_uniquechars:
        if char in ALPHABET:
            ALPHABET = ALPHABET.replace(char, '')
    return len(ALPHABET) == 0
