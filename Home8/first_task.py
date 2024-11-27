"""
тела человека. Пользователь вводит рост и вес с клавиатуры.
На выходе – ИМТ и пояснение к нему в зависимости от
попадания в тот или иной диапазон. Использовать обработку
исключений.
"""

try:
    user_weight = float(input("Enter weight (kg): "))
    user_height = float(input("Enter height (m): "))
    imt = user_weight / (user_height ** 2)

    if imt < 0:
        raise ValueError

    if imt < 16.5:
        user_imt_catg = "Super low weight!"
    elif 16.5 < imt < 18.5:
        user_imt_catg = "Low weight"
    elif 18.5 <= imt < 24.9:
        user_imt_catg = "Normal weight"
    elif 25 <= imt < 29.9:
        user_imt_catg = "Light overweight"
    elif 30 <= imt < 34.9:
        user_imt_catg = "Overweight, 1 step!"
    elif 35 <= imt < 39.9:
        user_imt_catg = "Overweight, 2 step!"
    else:
        user_imt_catg = "Overweight, 3 step or more!"

    print(f"Body weight index: {imt}\n"
          f"Index category: {user_imt_catg}")
except ValueError:
    print(f"Exception. Enter correct value")
