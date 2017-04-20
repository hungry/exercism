def distance(left, right):  # type: (str, str) -> int
    """Calculates the Hamming difference between two DNA strands"""

    if len(left) != len(right):
        raise ValueError('Input strings are not equal')

    diff = 0
    for i in range(0, len(left)):
        if left[i] != right[i]:
            diff += 1

    return diff
