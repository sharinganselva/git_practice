def count_islands(my_matrix):
    if not my_matrix:
        return 0

    rows = len(my_matrix)
    cols = len(my_matrix[0])
    print(f"rows = {rows}, cols = {cols}")
    count = 0

    for i in range(rows):
        for j in range(cols):
            if my_matrix[i][j] == "1":
                print("Found 1")
                count += 1
                find_and_sink_island(my_matrix, i, j, rows, cols)
    return count


def find_and_sink_island(my_matrix, i, j, rows, cols):
    if i < 0 or i >= rows or j < 0 or j >= cols or my_matrix[i][j] == "0":
        return

    my_matrix[i][j] = "0"
    find_and_sink_island(my_matrix, i-1, j, rows, cols)
    find_and_sink_island(my_matrix, i+1, j, rows, cols)
    find_and_sink_island(my_matrix, i, j-1, rows, cols)
    find_and_sink_island(my_matrix, i, j+1, rows, cols)


if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "1", "1", "1"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "1", "1", "1"]
    ]
    print(f"The could of Islands = {count_islands(grid)}")
