age = input ("Enter your age (enter q to exit): ")
if age == "q" or age == "Q":
    print("Exiting the program.")
    exit()


while age == "":
    print("Age cannot be empty. Please enter your age.")
    age = input("Enter your age (enter q to exit): ")
    if age == "q":
        print("Exiting the program.")
        exit()
if age.isalpha():
    print("Invalid input. Please enter a valid age.")
elif round(float(age)) < 18:
    print("You are a minor.")
else:
    print("You are an adult.")