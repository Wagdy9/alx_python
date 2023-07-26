import sys

def print_arguments():
    num_arguments = len(sys.argv) - 1

    print("Number of argument(s):", num_arguments)

    if num_arguments == 0:
        print(".")
        return

    print("Arguments:")

    for i in range(1, num_arguments + 1):
        print(i, ":", sys.argv[i])

print_arguments()