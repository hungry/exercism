def hey(phrase):  # type: (str) -> str
    """Bob is a lackadaisical teenager. In conversation, his responses are very limited."""

    phrase = phrase.strip()

    if len(phrase) == 0:
        return "Fine. Be that way!"

    if phrase.isupper():
        return "Whoa, chill out!"

    if phrase.endswith("?"):
        return "Sure."

    return "Whatever."
