Number = input("Enter a number between 1 and 10: ")
while round(float(Number)) < 1 or round(float(Number)) > 10:
    print("Invalid input. Please enter a number between 1 and 10.")
    Number = input("Enter a number between 1 and 10")
