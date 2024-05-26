my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
n = len(my_list)
a = 0
while my_list[a] >= 0 or a > n:
    if my_list[a] != 0:
        print(my_list[a])
    a = a + 1



