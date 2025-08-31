import time
from my_decorator import time_taken_decorator


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


def sum_of_embedded_numbers(my_string):
    embedded_number = ""
    total = 0

    if not my_string:
        print("The string is empty")
        return total

    for index, letter in enumerate(my_string):
        if letter.isdigit():
            embedded_number = embedded_number + letter
        else:
            if embedded_number != "":
                total += int(embedded_number)
                embedded_number = ""

        if index == len(my_string) - 1 and embedded_number != "":
            total += int(embedded_number)

    return total


def reverse_string(my_string):
    if not my_string:
        print("The string is empty")
        return

    return_string = ""
    for c in my_string:
        return_string = c + return_string

    return return_string


def first_non_repeat(my_string):
    if not my_string:
        return None
    elif len(my_string) == 1:
        return my_string[0]

    count = 0
    current_char = my_string[0]

    for i in range(1, len(my_string)):
        if my_string[i] == current_char:
            count += 1
        elif my_string[i] != current_char and count == 0:
            return current_char
        elif my_string[i] != current_char and count > 0:
            current_char = my_string[i]
            count = 0

        if count == 0 and i >= len(my_string)-1:
            return current_char

    return None


def is_palindrome(my_string):
    if not my_string:
        return False

    start = 0
    end = len(my_string) - 1
    while start <= end:
        if my_string[start] != my_string[end]:
            return False

        start += 1
        end -= 1

    return True


def is_anagram(str_a, str_b):
    if not str_a or not str_b:
        return False

    dict_a = {}
    for c in str_a:
        if c in dict_a:
            dict_a[c] += 1
        else:
            dict_a[c] = 1

    for c in str_b:
        if c not in dict_a:
            print(f"The character {c} is not present in the dictionary")
            return False
        else:
            dict_a[c] -= 1

    for key, value in dict_a.items():
        if value != 0:
            print(f"The character {key} is not the same in both strings")
            return False

    return True


@time_taken_decorator
def count_words(my_sentence):
    """
    1. This is a simple sentence
    2. This isn't a simple sentence.
    3. I have 2 or 3 breaks in a day. 
    """

    my_list = my_sentence.split(" ")
    my_dict = {}
    for item in my_list:
        if item in my_dict:
            my_dict[item] += 1
        else:
            my_dict[item] = 1

    for k, v in my_dict.items():
        print(f"The word \"{k}\" appears {v} times")


if __name__ == "__main__":
    print(high_freq_characters(""))
    print(f"Sum of all digits = {sum_of_embedded_numbers("a10ab100z0")}")
    print(unique_tuples({"a": 1, "b": 2}, {"a": 2, "b": 2, "c": 3}))
    print(f"Reversed String = {reverse_string("Hi My Dear!")}")
    print(f"First Non Repeating Character is = {first_non_repeat("aabbcC")}")
    print(f"The given string is a palindrome - {is_palindrome("aba")}")
    print(
        f"The given strings are anagrams - {is_anagram("aba12q3we", "qweaba123")}")
    print(
        f"The word count = {count_words("word is a word in the sentence a is in my IS")}")
