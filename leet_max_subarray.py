def max_sub_array(my_array):
    current_sum = 0
    max_sum = float('-inf')

    for i in my_array:
        current_sum = max(i, current_sum + i)
        max_sum = max(current_sum, max_sum)

    return max_sum


if __name__ == "__main__":
    print(f"Max Sum = {max_sub_array([-1, 0, 1, 3, 5])}")
