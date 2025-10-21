def find_transactions(transaction_list, target):
    dict = {}
    my_set = set()

    for i in transaction_list:
        if target - i in dict.keys():
            my_set.add((target - i, i))
        else:
            dict[i] = 0

    return my_set


if __name__ == "__main__":
    print(find_transactions([12, 34, 75, 98, 25, 2, 88], 100))
