def find_duplicates(arr):
    duplicates = []
    for i, value in enumerate(arr):
        index = abs(value)
        if arr[index] < 0:
            duplicates.append(index)
        else:
            arr[index] = -arr[index]
    return duplicates


if __name__ == "__main__":
    print(f"The duplicates are: {find_duplicates([1, 3, 2, 3, 4, 5, 5])}")
