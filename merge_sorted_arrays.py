def merge_sorted_array(arr1, arr2):
    arr3 = []
    i = j = 0
    while i < len(arr1) or j < len(arr2):
        print(
            f"i = {i}; j = {j}; len(arr1) = {len(arr1)}; len(arr2) = {len(arr2)}; arr3 = {arr3}")
        if i >= len(arr1):
            while j < len(arr2):
                arr3.append(arr2[j])
                j += 1

        if j >= len(arr2):
            while i < len(arr1):
                arr3.append(arr1[i])
                i += 1

        if i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                arr3.append(arr1[i])
                i += 1
            else:
                arr3.append(arr2[j])
                j += 1
    return arr3


if __name__ == "__main__":
    arr1 = [2, 5, 8, 14, 20, 100]
    arr2 = [1, 2, 3, 4, 5, 6, 7, 8]
    print(f"The Merged Array = {merge_sorted_array(arr1, arr2)}")
