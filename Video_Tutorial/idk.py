my_list = [0, 3, -10, 11, 60, 20]

def selection(my_list):
    for x in range(len(my_list)):
        min_index = x
        for y in range(x+1, len(my_list)):
            if my_list[y] < my_list[min_index]:
                min_index = y
        temp = my_list[x]
        my_list[x] = my_list[min_index]
        my_list[min_index] = temp
    return my_list
print(selection(my_list))