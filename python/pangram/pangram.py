import string


def is_pangram(phrase):  # type: (str) -> bool
    letters = set([letter for letter in phrase.lower() if letter.isalpha()])
    return letters == set(string.ascii_lowercase)
