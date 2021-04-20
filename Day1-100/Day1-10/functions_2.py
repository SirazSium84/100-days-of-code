import math


def greet(name_1, name_2, name_3):
    print(f"Welcome to our house {name_1}!")
    print(f"Please make yourself comfortable {name_2}.")
    print(f"I hope you had a great time {name_3}.")


greet(name_3="Sium", name_2="Sunan", name_1="Nazneen")


def paint(height, width, coverage):
    area = height * width
    cans = math.ceil(area/coverage)
    print(f"You will need {cans} cans of paint.")


test_h = int(input('Height of the wall: \n'))
test_w = int(input("Widhth of the wall: \n"))
coverage = 5
paint(test_h, test_w, coverage)


def prime_checker(number):
    for i in range(2, number):
        if number % i == 0:
            return "The number is not Prime."
        else:
            return "The number is Prime."


print(prime_checker(number=67))
