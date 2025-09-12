def water_container_area(my_list):
    max_area = 0
    left, right = 0, len(my_list) - 1
    while left < right:
        max_area = max(max_area, ((right-left) *
                       min(my_list[left], my_list[right])))
        if my_list[left] < my_list[right]:
            left += 1
        else:
            right -= 1
    return max_area


if __name__ == "__main__":
    print(
        f"The maximum area = {water_container_area([1, 8, 6, 2, 5, 4, 8, 3, 7])}")
