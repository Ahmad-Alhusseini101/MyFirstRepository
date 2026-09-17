Food = []
Price1 = 0
while True:
    item = input("Enter a food you'd like to buy (press q to quit): ")
    if item.lower() == "q":
        break
    else: 
        Food.append(item)
        price = round(float(input(f"Enter the price if a/an {item}: "))) + Price1
print("Here's your whole shopping list: ", end="")
for items in Food:
    if Food[-1] == items:
        print(f"and {items}", end=". ")
    elif len(Food) > 2:
        print(f"{items}", end=", ")
    else: 
        print(f"{items}", end=" ")
print("Your total price is:", price)