from collections import deque


def validate_brackets(my_string):
    if not my_string:
        return "The string is empty"

    my_dict = {"{": "}", "(": ")", "[": "]"}
    q = deque()

    q.append(my_string[0])
    i = 1

    while i < len(my_string):
        if my_string[i] in my_dict.keys():
            q.append(my_string[i])
            print(f"printing q: {q}")
        else:
            if q:
                top = q[-1]
                if my_dict[top] == my_string[i]:
                    temp = q.pop()
                    print(f"printing popped q: {temp}")
                else:
                    q.append(my_string[i])
                    print(f"printing q: {q}")
            else:
                q.append(my_string[i])
                print(f"printing q: {q}")
        i += 1

    if len(q) > 0:
        return False

    return True


if __name__ == "__main__":
    my_string = "{(()}{[()]}"
    print(f"The string validation: {validate_brackets(my_string)}")
