def high_freq_characters(my_string):
    print(f"{my_string}")
    # convert the string to dictionary
    if not my_string:
        print("String is Empty")
        return None

    my_dict = {}
    for letter in my_string:
        if letter in my_dict:
            my_dict[letter] += 1
        else:
            my_dict[letter] = 1

    max_value = max(my_dict.values())
    my_list = [k for k, v in my_dict.items() if v == max_value]
    return my_list


def sum_embedded_numbers(my_string):
    total = 0
    temp = ""

    for i in my_string:
        if not i.isdigit():
            print(i)
            if temp != "":
                total += int(temp)
            temp = ""
        else:
            temp = temp + i

        if i == my_string[-1] and temp != "":
            total += int(temp)

        # if i.isdigit():
        #     print("Found Digit")
        #     temp = temp + i
        # else:
        #     if temp != "":
        #         total += int(temp)
        #     temp = ""

    return total


def unique_tuples(dict1, dict2):
    result = []
    for k, v in dict1.items():
        if k not in dict2.keys() or v != dict2[k]:
            result.append((k, v))

    for k, v in dict2.items():
        if k not in dict1.keys() or v != dict1[k]:
            result.append((k, v))

    return result


if __name__ == "__main__":
    print(high_freq_characters(""))
    print(f"Sum of all digits = {sum_embedded_numbers("a123b10")}")
    print(unique_tuples({"a": 1, "b": 2}, {"a": 2, "b": 2, "c": 3}))
