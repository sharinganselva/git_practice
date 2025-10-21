def longest_substring(my_string):
    start = 0
    my_dict = {}
    longest_string = ""
    max_len = 0

    if my_string == "" or my_string is None:
        return 0

    for end, value in enumerate(my_string):
        if value not in my_dict and end == len(my_string) - 1:
            print(f"Adding {value} to dictionary")
            my_dict[value] = end

        if value in my_dict:
            print(f"Duplicate Entry {value} found")
            current_length = len(my_dict)
            print(f"current_length = {current_length}; max_len = {max_len}")
            if current_length > max_len:
                max_len = current_length
                longest_string = my_string[start:start+current_length]
                print(f"Intermediate longest string = {longest_string}")
            start = end
            my_dict.clear()
            print(f"Length after clearing the dictionary: {len(my_dict)}")
            print(f"Adding {value} to dictionary")

        print(f"Adding {value} to dictionary")
        my_dict[value] = end

    return max_len, longest_string


if __name__ == "__main__":
    print(longest_substring("noabccec"))
