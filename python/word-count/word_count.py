from collections import Counter
from re import split


def word_count(phrase):  # type: (str) -> dict
    """Given a phrase, counts the occurrences of each word in that phrase."""
    return Counter(word for word in split("[\W_]", phrase.lower()) if len(word) > 0)
