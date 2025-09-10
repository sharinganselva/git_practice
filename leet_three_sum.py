def three_sum(my_list):
    my_list.sort()
    output = []
    print(my_list)

    for i in my_list:
        left, right = i + 1, len(my_list) - 1
        while left < right:
            sum = my_list[i] + my_list[left] + my_list[right]
            if sum == 0:
                output.append([my_list[i], my_list[left], my_list[right]])

            if sum < 0:
                left += 1
            else:
                right -= 1

    return output


if __name__ == "__main__":
    print(three_sum([-2, 0, 7, 2, 4, -7, -6]))
