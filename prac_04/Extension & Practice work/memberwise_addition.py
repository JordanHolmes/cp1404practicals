first_list = [1, 2, 3]
second_list = [1, 2, 3, 4]

def memberwiseAddition(List_1, List_2):
    new_list = []
    for i in range(0, len(List_1)):
        new_list.append(List_1[i] + List_2[i])
    return new_list


finished_list = memberwiseAddition(first_list, second_list)
print(finished_list)