def longest_substring_without_repeat(my_string):
    longest_substring = ""
    current_substring = my_string[0]
    current_char = my_string[0]

    for i in range(1, len(my_string)):
        print(f"i is {i}")
        if current_char == my_string[i]:
            longest_substring = current_substring if len(
                current_substring) > len(longest_substring) else longest_substring
            current_substring = ""
        else:
            current_substring += my_string[i]
            current_char = my_string[i]

    longest_substring = current_substring if len(
        current_substring) > len(longest_substring) else longest_substring
    return longest_substring


if __name__ == "__main__":
    print(
        f"The longest substring is {longest_substring_without_repeat("abccdefghaabc")}")
