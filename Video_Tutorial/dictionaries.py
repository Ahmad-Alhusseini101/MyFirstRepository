food = {"meat": 1, "vegies": 2, "fruits": 3}
if food.get("sigma_boy"):
    print("Ohio")
else:
    for keys, values in food.items():
        print(f"{keys}: {values}")
food.pop("meat")
print(food)
food.update({"fish": 1})
print(food)
