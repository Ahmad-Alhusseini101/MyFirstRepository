Card_No = input("Enter your credit card No.: ")

    


index = 0
odd_sum = 0
sum_of_the_double_even_digits = 0

for x in range(1, len(Card_No)+1):
    if -x % 2 == 1:
        odd_sum += int(Card_No[-x])


for y in range(1, len(Card_No)+1):
    if -y % 2 == 0:
        if int(Card_No[-y]) * 2 >= 10:
            sum_of_the_double_even_digits += int(str(int(Card_No[-y]) * 2)[0]) + int(str(int(Card_No[-y]) * 2)[1])
        else:
            sum_of_the_double_even_digits += 2 * int(Card_No[-y])
whole_sum = odd_sum + sum_of_the_double_even_digits

if whole_sum % 10 == 0:
    print("Valid")
else:
    print("Invalid")

