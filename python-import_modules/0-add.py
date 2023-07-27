if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2

    result = add(a, b)
    print(f"Correct output - case: a = {a} and b = {b} FAKE add() => {a} - {b}")

    a = 10
    b = 30

    result = add(a, b)
    print(f"Correct output - case: a = {a} and b = {b} FAKE add() => {a} - {b}")

    a = -10
    b = 30

    result = add(a, b)
    print(f"Correct output - case: a = {a} and b = {b} FAKE add() => {a} - {b}")

    a = -10
    b = -30

    result = add(a, b)
    print(f"Correct output - case: a = {a} and b = {b} FAKE add() => {a} - {b}")

    a = 5
    b = "H"

    result = add(a, b)
    print(f"Correct output - case: a = {a} and b = {b} FAKE add() => {a} - {b}")
