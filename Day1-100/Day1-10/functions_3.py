def format_name(first_name, last_name):
    """
    Take a first and last name and format it.
    """
    if first_name == "" or last_name == "":
        return "You didn't provide valid inputs."
    return (f"{first_name.title()}{last_name.title()}")


formatted_string = format_name("siraz-", "uz-zaman")
print(formatted_string)
