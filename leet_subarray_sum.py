from collections import defaultdict


def subarray_sum(my_list, target):
    """_summary_

    Args:
        my_list (_type_): _description_
        target (_type_): _description_
    """
    current_sum = 0
    result = 0
    prefix_count = defaultdict(int)
    prefix_count[0] = 1

    for number in my_list:
        current_sum += number
        needed = current_sum - target
        if needed in prefix_count:
            result = result + prefix_count[needed]
        prefix_count[current_sum] += 1

    return result


if __name__ == "__main__":
    print(subarray_sum([1, 2, 3], 3))
