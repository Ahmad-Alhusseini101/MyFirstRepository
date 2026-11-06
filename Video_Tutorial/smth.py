my_list = [0, 3, -10, 11, 60, 20]
def bubble(my_list):
    for x in range(len(my_list)):
        for y in range(x+1, len(my_list)):
            if my_list[y] < my_list[x]:
                temp1 = my_list[y]
                temp2 = my_list[x]
                my_list[x] = temp1
                my_list[y] = temp2
    return my_list
print(bubble(my_list))