def is_balanced_paranthesis(my_string):
    para_dict = {"{": "}", "[": "]", "(": ")"}
    stack = []
    for i, value in enumerate(my_string):
        if value in para_dict.keys():
            stack.append(value)
        else:
            last = stack[-1]
            print(f"last = {last}")
            if last in para_dict.keys() and para_dict[last] == value:
                stack.pop()
            else:
                stack.append(value)

    if len(stack) == 0:
        return True

    return False


if __name__ == "__main__":
    the_string = "{[()]}"
    print(f"{is_balanced_paranthesis(the_string)}")
    print("Thank You")
