import sys


def print_arguments():
    arguments = sys.argv[1:]  # Exclude the script name from the arguments list
    num_arguments = len(arguments)

    # Print the number of arguments
    if num_arguments == 0:
        print("0 arguments.")
    else:
        if num_arguments == 1:
            print("1 argument:")
        else:
            print(f"{num_arguments} arguments:")

        # Print each argument with its position
        for i, arg in enumerate(arguments, start=1):
            print(f"{i}: {arg}")


if __name__ == "__main__":
    print_arguments()
