def get_valid_name():
    while True:
        name = input("name: ")
        if " " in name and len(name.split()) == 2:
            return name
        else:
            print("invalid input, use only letters.")


def get_valid_birthday():
    while True:
        birthday = input("birthday (DD-MM-YYYY): ")
        try:
            from datetime import datetime
            datetime.strptime(birthday, "%d-%m-%Y")
            return str(birthday).replace('-', '.')
        except ValueError:
            print("invalid date, use DD-MM-YYYY format.")


def get_valid_height():
    while True:
        try:
            height = int(input("height (cm): "))
            if height > 0:
                return height
            else:
                raise ValueError
        except ValueError:
            print("invalid input, use integer.")


def get_valid_weight():
    while True:
        try:
            weight = float(input("Weight (kg): "))
            if weight > 0:
                return weight
            else:
                raise ValueError
        except ValueError:
            print("Invalid input, use float.")


def get_valid_car():
    while True:
        car = input("own a car? (yes/no): ").strip().lower()
        if car == "yes":
            return True
        elif car == "no":
            return False
        else:
            print("invalid input, use 'yes' or 'no'.")


def get_valid_languages():
    while True:
        languages = input("languages (separated by space): ").strip()
        if languages:
            return languages.split()
        else:
            print("invalid input, use at least one language.")

