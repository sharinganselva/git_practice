def binary_search(my_list, target):
    if len(my_list) == 0:
        return False

    pivot = int(len(my_list) / 2)
    if my_list[pivot] == target:
        print("The target is found")
        return True
    elif my_list[pivot] > target:
        return binary_search(my_list[:pivot], target)
    else:
        return binary_search(my_list[pivot+1:], target)


def binary_search_iterative(my_list, target):
    left, right = 0, len(my_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if my_list[mid] == target:
            return True
        elif my_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


def search_rotated_array(my_list, target):
    left, right = 0, len(my_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if my_list[mid] == target:
            return mid
        elif my_list[mid+1] <= target <= my_list[right]:
            left = mid + 1
        else:
            right = mid - 1

    return False


if __name__ == "__main__":
    print(f"Found the target? : {binary_search([1, 2, 3, 5, 7, 9], 9)}")
    print(
        f"Found the target? : {binary_search_iterative([1, 2, 3, 5, 7, 9], 9)}")
    print(
        f"Found the target? : {search_rotated_array([9, 10, 14, 15, 25, 39, 1, 2, 3, 5, 7, ], 1)}")
