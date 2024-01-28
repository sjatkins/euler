from datetime import date


def month_starts_days(start, end, day_num=7):
    s_year, s_month = start
    e_year, e_month = end
    count = 0
    for year in range(s_year, e_year + 1):
        end_month = e_month + 1 if year == e_year else 13
        for month in range(s_month, end_month):
            day = date(year, month, 1)
            if day.weekday() == 6:
                count += 1
    return count


def hard_way(start, end):
    has_30 = 4, 6, 9, 11
    has_31 = 1, 3, 5, 7, 8, 12

    def is_leap(year):
        if not year % 100:
            return not year % 400
        else:
            return not year % 4

    def month_len(month_num, year):
        if month_num == 2:
            return 29 if is_leap(year) else 28
        elif year in has_30:
            return 30
        else:
            return 31

    def days_since_beginning(year, month, day=1):
        days = 0
        for y in range(1900, year):
            days += (366 if is_leap(y) else 365)
        for m in range(1, month):
            days += month_len(m, year)
        days += day - 1
        return days

    def inc_month(year, month):
        month = (month + 1) % 12 + 1
        if month == 1:
            year += 1
        return year, month

    month_num = lambda year, month: year * 12 + month

    s_year, s_month = start
    e_year, e_month = end
    years = e_year - s_year
    months = month_num(e_year, e_month) - month_num(s_year, s_month) + 1

    until_start = days_since_beginning(s_year, s_month)
    count = 0
    weekday = (1 + until_start) % 7
    if not weekday:
        count += 1

    year, month = s_year, s_month

    for _ in range(months):
        days = month_len(month, year)
        weekday = (weekday + days) % 7
        if not weekday:
            count += 1
        year, month = inc_month(year, month)

    return count


def solve():
    assert month_starts_days((1900, 1), (1900, 12)) == 2
    assert hard_way((1900, 1), (1900, 12)) == 2
    return month_starts_days((1901, 1), (2000, 12))


solve(), hard_way((1901, 1), (2000, 12))
