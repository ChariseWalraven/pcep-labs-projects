def is_year_leap(year):
    result = False
    if year % 4 == 0:
        if year % 100 != 0 or (year % 100 == 0 and year % 400 == 0):
            result = True
    return result

def days_in_month(year, month):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif is_year_leap(year):
        return 29
    else:
        return 28
