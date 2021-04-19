from secret_auction_art import logo
from os import system, name

print(logo)


def clear():
    system("clear") if name == "posix" else system("cls")


bidding = {}


def find_the_highest_bidder():
    highest = 0
    for price, name in bidding.items():
        if int(price) > highest:
            highest = int(price)
    print(
        f"The winner is {bidding[str(highest)]} with the bid amount of ${highest}.")


while True:
    name = input("What is your name?: ")
    price = input("Please enter your bid price in USD: ").replace(
        '$', '')
    bidding[price] = name
    if_more = input("Are there any more bidders?\nYes or No?\n").lower()
    if if_more == "no":
        find_the_highest_bidder()
        break
    clear()
