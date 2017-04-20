from datetime import timedelta, datetime


def add_gigasecond(moment):  # type: (datetime) -> datetime
    """Calculate the moment when someone has lived for 10^9 seconds."""
    return moment + timedelta(seconds=10 ** 9)
