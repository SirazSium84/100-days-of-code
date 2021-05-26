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
    if month < 1 or month > 12:
        return "Invalid Input."
    elif month == 2:
        if is_leap(year) == True:
            return 29
        return 28
    elif month % 2 == 0:
        return 30
    return 31


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
