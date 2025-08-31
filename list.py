from my_decorator import log_decorator


@log_decorator
def find_duplicates(my_list):
    my_dict = {}
    my_set = set()

    for n in my_list:
        if n in my_dict.keys():
            my_set.add(n)
        else:
            my_dict[n] = 0

    return my_set


def two_sum(my_list, target):
    if not my_list:
        print("The list is empty")

    my_dict = {}
    i = 0
    for n in my_list:
        if target - n in my_dict:
            print(f"The two indices are {i}, {my_dict[target-n]}")
            return True
        else:
            my_dict[n] = i
            i += 1

    print("Cannot find two numbers that sum to the target")
    return False


def move_zeroes(the_list):
    result = []
    count = 0
    for n in the_list:
        if n == 0:
            count += 1
        else:
            result.append(n)

    while count > 0:
        result.append(0)
        count -= 1

    return result


def move_zeroes_in_position(the_list):
    current_index = 0
    for n in the_list:
        if n != 0:
            the_list[current_index] = n
            current_index += 1

    while current_index < len(the_list):
        the_list[current_index] = 0
        current_index += 1

    return the_list


def consecutive_ones(the_list):
    max_count = current_count = 0
    for n in the_list:
        if n == 1:
            current_count += 1
        else:
            max_count = max(max_count, current_count)
            current_count = 0
    return max_count


def missing_number(n, my_list):
    if n != len(my_list) + 1:
        print("Incorrect Inputs")
        return 0
    actual_total = 0
    expected_total = n * (n + 1)/2
    for i in my_list:
        actual_total += i

    return int(expected_total - actual_total)


if __name__ == "__main__":
    print(f"The duplicates are: {find_duplicates([2, 3, -1, -1, 1, 2, 4, 3])}")
    two_sum([4, 6, 5, 4], 11)
    print(
        f"The moving zeroes result = {move_zeroes([0, 0, 0, 0, 0, 0, 3, 0, 0])}")
    print(
        f"The moving zeroes in position result = {move_zeroes_in_position([1, 0, 0, 2, 0, 0, 3, 0, 0])}")
    print(
        f"Consecutive Ones = {consecutive_ones([1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0])}")
    print(f"The missing number is {missing_number(5, [1, 2, 5, 4])}")
