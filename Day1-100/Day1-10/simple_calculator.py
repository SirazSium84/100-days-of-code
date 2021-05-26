def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = ["+", "-", "*", "/"]
result = {"first_number": None}
while True:
    if result["first_number"] is None:
        result["first_number"] = int(input("What's the first number: "))
        output = 0
    for x in operations:
        print(x)
    operator = input("Pick an operation: ")
    result["next_number"] = int(input("What's the next number?: "))
    if operator == "+":
        output += add(result["first_number"], result["next_number"])
    elif operator == "-":
        output += sub(result["first_number"], result["next_number"])
    elif operator == "*":
        output += multiply(result["first_number"], result["next_number"])
    elif operator == "/":
        output += divide(result["first_number"], result["next_number"])
    print(
        f"{result['first_number']} {operator} {result['next_number']} = {output}")
    decision = input(
        f"Type 'y' to continue calculating with {output} or type 'n' or type 'e' to end calculator: ")
    if decision == "y":
        result["first_number"] = output
        output = 0
        continue
    elif decision == "n":
        result["first_number"] = None
    else:
        break
