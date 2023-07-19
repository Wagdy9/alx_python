import random

# Generate a random number between -10 and 10
number = random.randint(-10, 10)

# Print the number along with its sign
print(
    f"{number} is {'negative' if number < 0 else 'zero' if number == 0 else 'positive'}"
)
