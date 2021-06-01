from os import system, name
from calculator_art import logo


def clear():
    system("clear") if name == "posix" else system("cls")


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {"+": add,
              "-": sub,
              "*": multiply,
              "/": divide}
result = {"first_number": None}


def calculator():
    while True:
        if result["first_number"] is None:
            print(logo)
            result["first_number"] = float(input("What's the first number: "))
            output = 0
        for symbol in operations:
            print(symbol)
        operator = input("Pick an operation from the line above: ")
        result["next_number"] = float(input("What's the next number?: "))
        calculation_function = operations[operator]
        answer = calculation_function(
            result["first_number"], result["next_number"])
        print(
            f"{result['first_number']} {operator} {result['next_number']} = {answer}")
        decision = input(
            f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation or type 'e' to end calculator: ")
        if decision == "y":
            result["first_number"] = answer
            output = 0
            continue
        elif decision == "n":
            result["first_number"] = None
            clear()
        else:
            print("Have a good day. Thanks!")
            break


calculator()
