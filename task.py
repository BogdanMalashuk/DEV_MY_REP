while True:
    name = input("Enter your name: ")

    if name.isalpha():
        print(f"Hi, {name}!")
        break
    else:
        print("Enter the correct name")
