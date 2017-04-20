def is_isogram(word):  # type: (str) -> bool
    """Checks whether supplied word is an isogram"""

    seen_letters = {}

    for letter in [letter for letter in word.lower() if letter.isalpha()]:
        if letter not in seen_letters:
            seen_letters[letter] = True
        else:
            return False

    return True
