# Task 1: Input Length Validator --------------------------------------------------------------------------------
def input_length_validator():
    first_name = len(input("Please enter your first name: "))
    last_name = len(input("Please enter your last name: "))
    if first_name <= 2:
        print("Error: First name must be at least 2 characters long.")
    if last_name <= 2:
        print("Error: Last name must be at least 2 characters long.")
    if first_name > 2 and last_name > 2:
        print("Both names are valid.")
# Run the validator function
input_length_validator()