# print("Welcome to the rollercoaster!")
# bill = 0
# try:
#     height = int(input("What is your height in cm? "))
#     if height >= 120:
#         print("You can ride the rollercoster.")
#     else:
#         print("Sorry you have to grow taller before you can ride.")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         print("Child Tickets are $5.")
#     elif 12 <= age <= 18:
#         bill = 7
#         print("Youth Tickets are $7.")
#     elif 45 <= age <= 55:
#         print("Everything is going to be OK. Have a free ride on us")
#     else:
#         bill = 12
#         print("Adult Tickets are $12.")
#     photo = input("Do you want a photo taken? Y or N\n")
#     if photo == "Y":
#         bill += 3
#         print("Your final bill is ${}".format(bill))
#     else:
#         print("Your final bill is ${}".format(bill))
# except:
#     print("Please enter a correct value!")


# # 🚨 Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# bmi = round(weight/(height**2), 2)
# if bmi < 18.5:
#     print("Your BMI is {bmi}, you are underweight".format(bmi=bmi))
# elif bmi < 25:
#     print("Your BMI is {bmi}, you have a normal weight".format(bmi=bmi))
# elif bmi < 30:
#     print("Your BMI is {bmi}, you are overweight".format(bmi=bmi))
# elif bmi < 35:
#     print("Your BMI is {bmi}, you are obese".format(bmi=bmi))
# else:
#     print("Your BMI is {bmi}, you are clinically obese".format(bmi=bmi))


# # 🚨 Don't change the code below 👇
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇

# total_bill = 0
# if size == "S":
#     total_bill += 15
#     if add_pepperoni == "Y":
#         total_bill += 2
#     if extra_cheese == "Y":
#         total_bill += 1
# elif size == "M":
#     total_bill += 20
#     if add_pepperoni == "Y":
#         total_bill += 3
#     if extra_cheese == "Y":
#         total_bill += 1
# elif size == "L":
#     total_bill += 25
#     if add_pepperoni == "Y":
#         total_bill += 3
#     if extra_cheese == "Y":
#         total_bill += 1

# print("Your total bill is: ${}".format(total_bill))


# # 🚨 Don't change the code below 👇
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# # 🚨 Don't change the code above 👆

# # Write your code below this line 👇
# both_name = (name1 + name2).lower()
# true_count = 0
# love_count = 0
# for x in "true":
#     true_count += both_name.count(x)

# for y in "love":
#     love_count += both_name.count(y)
# output_count = int(str(true_count) + str(love_count))

# if output_count < 10 or output_count > 90:
#     print("Your love score is {}, you go together like coke and mentos.".format(
#         output_count))
# elif 40 <= output_count <= 50:
#     print("Your love score is {}, you are alright together.".format(output_count))
# else:
#     print("Your love score is {}.".format(output_count))


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first_bridge = input(
    "You find two ways to a bridge, which way are you going to go ? \"Left\" or \"Right\" ?\n").lower()
if first_bridge == "left":
    print("You go to the end of the bridge.")
    swim_wait = input(
        "You can wait for help or can swim across the river. What are you going to do? \"Swim or \"Wait?\n").lower()
    if swim_wait == "wait":
        print('''You find a boat passing by. With it's help reach the other side of the river. 
        You find a cave with three doors of three colors. \"Red\", \"Blue\" and \"Yellow\".''')
        door = input("Which one do you choose?\n").lower()
        if door == "red":
            print("You got burned by fire. Game over!")
        elif door == "blue":
            print("You became dinner for beasts hiding in the dark. Game over!\n")
        elif door == "yellow":
            print("Good Job! You made it! You won!")
        else:
            print("Game over !")
    else:
        print("You got attacked by a trout! Game over! What were you even thinking?\n")
else:
    print("You fall into a hole. Game over! You suck !")
