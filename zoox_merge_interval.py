def merge_interval(my_list):
    merged_list = []
    my_list.sort()
    print(my_list)
    i = 0
    j = 1
    while i <= len(my_list) - 1:
        temp_list = []
        print(f"Temp List = {merged_list} and i = {i}")
        temp_list.append(my_list[i])
        while True:
            try:
                if j <= len(my_list) - 1 and my_list[i][1] >= my_list[j][0]:
                    temp_list.append(my_list[j])
                    i += 1
                    j += 1
                else:
                    start = temp_list[0][0]
                    end = temp_list[len(temp_list) - 1][1]
                    merged_list.append([start, end])
                    i = j
                    j = i + 1
                    break
            except IndexError:
                print(f"Index Error at j = {j} ")
                break

    return merged_list


if __name__ == "__main__":
    print(f"The merged list = {merge_interval(
        [(1, 2), (2, 5), (3, 7), (8, 12), (15, 19), (13, 18)])}")
