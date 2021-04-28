def is_leap(year):
    if year % 4 == 0:
        # if year % 100 == 0:
        #     if year % 400 == 0:
        #         return True
        #     else:
        #         return False
        # else:
        #     return True
        return year % 100 == 0 and year % 400 == 0 or year % 100 != 0
    else:
        return False


def days_in_month(year, month):
    if is_leap(year) == True and month == 2:
        return 29
    elif month == 2:
        return 28
    elif month % 2 == 0:
        return 30
    else:
        return 31


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


# return year % 100 == 0 and year % 400 == 0 or year % 100 != 0
