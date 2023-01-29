def is_year_leap(year):
    result = False
    if year % 4 == 0 and year > 1582:
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

def day_of_year(year, month, day):
  if not (days_in_month(year, month) >= day > 0 and 0 < month <= 12):
    return None
  for i in range(month - 1):
    day += days_in_month(year, i+1)
  return day