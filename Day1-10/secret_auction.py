from os import system, name


def clear():
    system("clear") if name == "posix" else system("cls")


bidding = {}
highest = 0

while True:
    name = input("What is your name?\n")
    price = input("Please enter your bid price.\n").replace(
        '$', '')
    bidding[price] = name
    if_more = input("Are there any more bidders?\nYes or No?\n").lower()
    if if_more == "no":
        break
    clear()

for price, name in bidding.items():
    if int(price) > highest:
        highest = int(price)
print(bidding[str(highest)])
