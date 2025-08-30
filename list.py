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


if __name__ == "__main__":
    print(f"The duplicates are: {find_duplicates([2, 3, -1, -1, 1, 2, 4, 3])}")
