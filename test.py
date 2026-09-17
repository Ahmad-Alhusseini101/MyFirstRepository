Food = []
while True:
    item = input("Enter a food you'd like to buy (press q to quit): ")
    if item.lower() == "q":
        break
    else: 
        Food.append(item)
        price = round(float(input(f"Enter the price if a/an {Food}: ")))
print(f"Here's your whole shopping list: {Food}, and the total price is: {price}")
