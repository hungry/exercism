from itertools import groupby
from re import split


def decode(data):  # type: (str) -> str
    """Reconstructs original data from the compressed data."""

    result = ''
    groups = (x for x in split(r"(\d+[\w\s]|[\w\s])", data) if len(x) > 0)

    for group in groups:
        if group[:-1].isdigit():
            result += group[-1] * int(group[:-1])
        else:
            result += group

    return result


def encode(data):  # type: (str) -> str
    """Consecutive data elements are replaced by count and one data value."""

    result = ''
    groups = ((label, sum(1 for _ in group)) for label, group in groupby(data))

    for char, count in groups:
        if count > 1:
            result += str(count) + char
        else:
            result += char

    return result
