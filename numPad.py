numbers = [[1, 2, 3], 
         [4, 5, 6], 
         [7, 8, 9], 
         ["*", 0, "#"]]
for lines in numbers:
    for number in lines:
        print(number, end=" ")
    print()