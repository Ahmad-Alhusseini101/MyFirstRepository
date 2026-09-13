price = input("Enter your initial investment price: ")

rate = input("Enter your annual interest rate: ")

while float(rate) <= 0:
    print("Invalid input. Please enter a valid interest rate.")
    rate = input("Enter your annual interest rate: ")

duration = input("Enter the duration in years: ")
while float(duration) <= 0:
    print("Invalid input. Please enter a valid duration.")
    duration = input("Enter the duration in years: ")


new_price = float(price) * (1 + float(rate)/100) ** float(duration)
print("Your new price is", new_price)