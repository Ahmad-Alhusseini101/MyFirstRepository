import random
number = random.randint(1, 100)
guesses = 0
while True:
    guess = round(float(input("Enter a number between 1 and 100: ")))
    guesses += 1
    if guess < 1 or guess > 100:
        print("Please enter a number withing the range")
    else:
        if guess > number:
            print("Your guess is higher than the number")
        elif guess < number:
            print("Your guess is lower than the number")
        else:
            print(f"You've got it! It took you {guesses} guesses")
            break