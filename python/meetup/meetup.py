from datetime import date, timedelta
from re import findall, match


class MeetupDayException(Exception):
    pass


def meetup_day(year, month, weekday, ordinal):  # type: (int, int, str, str) -> date
    """
    Calculate the date of meetups.
    """
    if ordinal == 'teenth':
        for possible_date in teenth_dates(year, month):
            if possible_date.strftime('%A') == weekday:
                return possible_date

    if ordinal == 'last':
        for possible_date in last_seven_days(year, month):
            if possible_date.strftime('%A') == weekday:
                return possible_date

    if match(r'\d+', ordinal):
        ordinal = int(findall(r'\d+', ordinal)[0])
        start_date = date(year, month, 1)
        seen_weekdays = 0

        if start_date.strftime('%A') == weekday:
            seen_weekdays += 1

        while start_date.month == month:
            if seen_weekdays == ordinal:
                return start_date

            start_date += timedelta(days=1)
            if start_date.strftime('%A') == weekday:
                seen_weekdays += 1

    raise MeetupDayException


def last_seven_days(year, month):
    """
    Generates last seven days
    """
    end_of_month = last_day(year, month)
    for day in (end_of_month - timedelta(days=diff) for diff in range(7)):
        yield day


def teenth_dates(year, month):
    """
    Generates all 'teenth' dates
    """
    for day in range(13, 20):
        yield date(year, month, day)


def last_day(year, month):  # type: (int, int) -> date
    """
    Returns the date of last day of given year and month
    """
    if year <= 0 or month <= 0:
        raise ValueError

    next_month = month + 1

    if next_month > 12:
        year += next_month / 12
        next_month = next_month % 12

    return date(year, next_month, 1) - timedelta(days=1)
