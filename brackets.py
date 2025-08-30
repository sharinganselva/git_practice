from collections import deque


def validate_brackets(my_string):
    print("All good")
    brackets = {"{": "}", "[": "]", "(": ")"}
    my_stack = deque()

    for i, current_char in enumerate(my_string):
        print(f"Current Character: {my_string[i]}")
        if len(my_stack) == 0:
            my_stack.append(current_char)
        else:
            top = my_stack[-1]
            if brackets[top] == current_char:
                my_stack.pop()
            else:
                my_stack.append(current_char)

    if len(my_stack) == 0:
        return True

    return False


if __name__ == "__main__":
    print(f"The brackets are well closed: {validate_brackets("({}[{}])")}")
