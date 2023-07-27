def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, num in enumerate(row):
            if i < len(row) - 1:
                print("{:d} ".format(num), end="")
            else:
                print("{:d}".format(num), end="")
        print()
    if not matrix:
        print()


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_matrix_integer(matrix)
print("--")

matrix = [[1, 2], [4, 5]]
print_matrix_integer(matrix)
print("--")

matrix = [[1, 2], [4, 5], [7, 8]]
print_matrix_integer(matrix)
print("--")

matrix = [[1]]
print_matrix_integer(matrix)
print("--")

matrix = [[1], [2], [3], [4]]
print_matrix_integer(matrix)
print("--")

matrix = [[]]
print_matrix_integer(matrix)
