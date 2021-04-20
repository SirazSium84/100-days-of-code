print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? \n$"))
percentage = int(input(
    "What percentage tip would you like to give ? 10, 12 or 15?\n"))
people = int(input("How many people to split the bill? \n"))
bill_per_person = (total_bill + total_bill * (percentage)/100)/(people)
print("Each person should pay : ${:.2f}".format(bill_per_person))


# # print(123_567_789)


# # 🚨 Don't change the code below 👇
# age = input("What is your current age?")
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇


# def time_left(age):
#     years_left = 90 - int(age)
#     months_left = years_left * 12
#     weeks_left = years_left * 52
#     days_left = years_left * 365
#     return days_left, weeks_left, months_left


# days, weeks, months = time_left(age)
# print(f"You have {days} days, {weeks} weeks, and {months} months left")
