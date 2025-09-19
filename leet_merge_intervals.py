def merge_intervals(my_list):
    """_summary_

    Args:
        my_list (_type_): _description_

    Returns:
        _type_: _description_
    """
    my_list.sort()
    new_list = []
    i = 0
    while i < len(my_list):
        j = i + 1
        temp_tuples_list = []
        temp_tuples_list.append(my_list[i])
        while True:
            if j < len(my_list) and my_list[j][0] <= my_list[i][1]:
                temp_tuples_list.append(my_list[j])
                i = j
                j += 1
            else:
                first = temp_tuples_list[0][0]
                second = temp_tuples_list[len(temp_tuples_list)-1][1]
                new_tuple = (first, second)
                new_list.append(new_tuple)
                i = j
                break
    return new_list


if __name__ == "__main__":
    print(merge_intervals(
        [(1, 3), (2, 6), (5, 10), (12, 15), (15, 20), (21, 30)]))
