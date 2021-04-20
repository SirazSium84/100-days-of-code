# import random
# random_integer = random.randint(1, 10)
# print(random_integer)
# random_float = random.random()
# print(random_float)
# random_float2 = random.uniform(0, 5)
# print(random_float2)
# love_score = random.randint(1, 100)
# print(love_score)


# # Write your code below this line 👇
# # Hint: Remember to import the random module first. 🎲
# import random
# random_int = random.randint(0, 1)
# if random_int == 0:
#     print("Heads")
# else:
#     print("Tails")


# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
#                      "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York",
#                      "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana",
#                      "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan",
#                      "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas",
#                      "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana",
#                      "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]


# print(states_of_america[0])

# states_of_america[1] = "Pencilvania"
# states_of_america.extend(["Deadpool Land", "SupermanLand"])
# states_of_america.insert(0, "Sium Land")

# print(states_of_america)


# import random
# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# number = len(names)
# random_choice = random.randint(0, number - 1)
# print(f"{names[random_choice]} is going to buy the meal today!")


# # better solution
# #name = random.choice(names)


# # 🚨 Don't change the code below 👇
# row1 = ["⬜️", "⬜️", "⬜️"]
# row2 = ["⬜️", "⬜️", "⬜️"]
# row3 = ["⬜️", "⬜️", "⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# # Write your code below this row 👇
# horizontal = int(position[1]) - 1
# vertical = int(position[0]) - 1
# map[horizontal][vertical] = "X"


# # Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")


import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
while True:
    user_input = int(
        input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
    if user_input not in range(3):
        print("Invalid Input. You lose!")
        break
    patterns = [rock, paper, scissors]
    print("You chose:\n")
    print(patterns[user_input], end="\n")
    computer_input = random.randint(0, 2)
    print("Computer chose:\n")
    print(patterns[computer_input], end="\n")
    if user_input == computer_input:
        print("It's a draw. Try Again!")
        continue
    elif user_input == 0 and computer_input == 1:
        print("Computer Wins!")
        break
    elif user_input == 0 and computer_input == 2:
        print("You Win!")
        break
    elif user_input == 1 and computer_input == 0:
        print("You Win!")
        break
    elif user_input == 1 and computer_input == 2:
        print("Computer Wins!")
        break
    elif user_input == 2 and computer_input == 0:
        print("Computer Wins!")
        break
    elif user_input == 2 and computer_input == 1:
        print("You Win!")
        break
