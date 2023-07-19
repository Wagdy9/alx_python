import random

# Generate a random number between -10,000 and 10,000
number = random.randint(-10000, 10000)

# Calculate the last digit of the number
last_digit = number % 10

# Print the last digit and its properties
print(f"Last digit of {number} is {last_digit} and is", end=" ")
if last_digit > 5:
 print("greater than 5")
elif last_digit < -5:
 print("less than -5")
elif last_digit == 0:
 print("0")
else:
 print("less than 6 and not 0")
