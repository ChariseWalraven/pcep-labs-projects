def is_year_leap(year):
    result = False
    if year % 4 == 0:
        if year % 100 != 0 or (year % 100 == 0 and year % 400 == 0):
            result = True
    return result
