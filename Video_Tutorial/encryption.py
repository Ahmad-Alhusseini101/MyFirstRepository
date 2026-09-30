import string
import random

characters = " " + string.ascii_letters + string.digits + string.punctuation 
characters_list = list(characters)
keys = characters_list.copy()
random.shuffle(keys)

lost = True
index = 0

user_input = input("Eneter a message: ")
for letter in user_input:
    while lost:
        if characters_list[index] == letter:
            break
        else:
            index += 1
    print(keys[index], end="")
    index = 0
print()
print(f"{characters_list}")
print()
print(f"{keys}")
