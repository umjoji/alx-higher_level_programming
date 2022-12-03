#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bool_list = []
    if len(my_list):
        for i in my_list:
            if i % 2 == 0:
                bool_list.append(True)
                continue
            bool_list.append(False)
    return bool_list

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)
print(list_result)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1

print()

for i in range(len(list_result)):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
