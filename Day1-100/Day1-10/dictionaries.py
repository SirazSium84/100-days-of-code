# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected",
#     "Function": "A piece of code that you can easily call over and over again"}

# # Retrieving items from dictionary
# print(programming_dictionary["Bug"])

# # Adding items to dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again."

# print(programming_dictionary)

# # Edit the item in a dictionary

# programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)


# empty_dictionary = {}

# # Wipe the existing dictionary

# programming_dictionary = {}

# # print(programming_dictionary)

# for key in programming_dictionary.items():
#     print(key)


# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# # 🚨 Don't change the code above 👆

# # TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}


# # TODO-2: Write your code below to add the grades to student_grades.👇
# for student in student_scores.items():
#     if student[1] >= 91:
#         student_grades[student[0]] = "Outstanding"
#     elif student[1] >= 81:
#         student_grades[student[0]] = "Exceeds Expectation"
#     elif student[1] >= 71:
#         student_grades[student[0]] = "Acceptable"
#     else:
#         student_grades[student[0]] = "Fail"


# # 🚨 Don't change the code below 👇
# print(student_grades)


# # Nesting
# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin"
# }

# # Nesting a List in a Dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"]
# }


# # Nesting Dictionary in a Dictionary
# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
# }
# # Accessing elements in a nested dictionary
# print(travel_log["France"]["cities_visited"][0])


# # Nesting a Dictionary inside a list.
# travel_log = [
#     {"country": "France",
#      "cities_visited": ["Paris", "Lille", "Dijon"],
#      "total_visits": 12},
#     {"country": "Germany",
#      "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#      "total_visits": 5}
# ]
# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"]
#     },
# ]
# # 🚨 Do NOT change the code above

# # TODO: Write the function that will allow new countries
# # to be added to the travel_log. 👇


# def add_new_country(country, visits, cities, travel_log=travel_log):
#     travel_log.append({"country": country, "visits": visits, "cities": cities})


# # 🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)
