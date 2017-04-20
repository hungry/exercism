from string import maketrans, ascii_lowercase as lc, ascii_uppercase as uc


def rotate(words, no):
    return words.translate(maketrans(lc + uc, lc[no:] + lc[:no] + uc[no:] + uc[:no]))
