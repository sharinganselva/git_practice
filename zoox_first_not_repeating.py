def find_first_non_repeating_char(my_string):
    count = 0
    for i, value in enumerate(my_string):
        if i+1 < len(my_string) and value != my_string[i+1]:
            if count == 0:
                return value
            else:
                count = 0
        elif i+1 >= len(my_string):
            if count == 0:
                return value
        else:
            count += 1
    return 0


if __name__ == "__main__":
    print(f"{find_first_non_repeating_char("aabbBcc")}")
    print("Thank You")
