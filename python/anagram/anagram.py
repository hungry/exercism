from collections import Counter


def detect_anagrams(word, candidates):
    return [candidate for candidate in candidates if compare(word.lower(), candidate.lower())]


def compare(first, second):
    return False if first == second else Counter(first) == Counter(second)
