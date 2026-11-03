#section 1

#setting up a list
scores = [0, 1, 2, 3, 4]
print(scores[2])
print()

#modifying an element

scores[0]= 100
for x in scores:
    print(x)
print()


#sum of the elements in the list
sum = 0
for y in scores:
    sum += y
print(sum)
print()


#average of all elements 
average = sum/len(scores)
print(average)
print()


#highest score

highest_score = scores[0]
for m in scores:
    if m > highest_score:
        highest_score = m

print(highest_score)

print()

# lowest score

lowest_score = scores[0]
for m in scores:
    if m < lowest_score:
        lowest_score = m

print(lowest_score)

print()

#checking an integer
integer = input("Enter an integer to check wether it's in the list or not: ")
answer = False
for k in range(len(scores)):
    if scores[k] == int(integer):
        answer=True

print(answer)
print()

#copy of the old list
new_scores = scores.copy()
new_scores[3] = 10
print(new_scores)
print(scores)
print()

#section 2
#setting up a 2D lis
grades = [[90, 85, 92, 78],
          [88, 91, 85, 95],
          [76, 80, 82, 85]]

#accesing an element

print(grades[1][2])

#changing values

grades[2][0] = 99

print()

# using for loops to print the elements

for x in grades:
    for y in x:
        print(y, end=" ")

print()

#sum of the row
sum_row = 0 
for x in grades:
    print(x[0])
    sum_row += x[0]
print(sum_row)