"""

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

"""


def product_array(my_array):
    """_summary_

    Args:
        my_array (_type_): _description_
    """
    result = []
    multiple = 1
    for i, val in enumerate(my_array):  # for i in range(0, len(my_array)):
        result.append(multiple)
        multiple *= val
    print(result)

    multiple = 1
    for i in range(len(my_array)-1, -1, -1):
        print(i)
        result[i] = result[i] * multiple
        multiple *= my_array[i]
    print(result)


if __name__ == "__main__":
    product_array([2, 5, 10, 3])
