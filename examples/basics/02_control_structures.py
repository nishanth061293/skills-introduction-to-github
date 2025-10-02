"""
Python Basics: Control Structures

This file demonstrates if statements, loops, and other control flow structures.
"""

# If Statements
print("=== If Statements ===")
temperature = 75

if temperature > 80:
    print("It's hot outside!")
elif temperature > 60:
    print("It's a nice day!")
else:
    print("It's a bit cold.")

# More if examples
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# For Loops
print("\n=== For Loops ===")
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"Count: {i}")

print("\nLoop through a list:")
fruits = ["apple", "banana", "orange", "grape"]
for fruit in fruits:
    print(f"I like {fruit}")

print("\nLoop with index:")
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

# While Loops
print("\n=== While Loops ===")
print("Countdown:")
countdown = 5
while countdown > 0:
    print(f"{countdown}...")
    countdown -= 1
print("Blast off!")

# Break and Continue
print("\n=== Break and Continue ===")
print("Numbers 1-10, but skip 5 and stop at 8:")
for i in range(1, 11):
    if i == 5:
        continue  # Skip 5
    if i == 8:
        break     # Stop at 8
    print(i)

# Nested Loops
print("\n=== Nested Loops ===")
print("Multiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print()  # Empty line after each row