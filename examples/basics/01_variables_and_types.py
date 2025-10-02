"""
Python Basics: Variables and Data Types

This file demonstrates the fundamental data types in Python
and how to work with variables.
"""

# Variables and Assignment
print("=== Variables and Assignment ===")
name = "Alice"
age = 25
height = 5.6
is_student = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height} feet")
print(f"Is student: {is_student}")

# Data Types
print("\n=== Data Types ===")
print(f"Type of name: {type(name)}")
print(f"Type of age: {type(age)}")
print(f"Type of height: {type(height)}")
print(f"Type of is_student: {type(is_student)}")

# Strings
print("\n=== Working with Strings ===")
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")
print(f"Full name (using f-string): {first_name} {last_name}")
print(f"Name length: {len(full_name)}")
print(f"Uppercase: {full_name.upper()}")
print(f"Lowercase: {full_name.lower()}")

# Numbers
print("\n=== Working with Numbers ===")
x = 10
y = 3

print(f"x = {x}, y = {y}")
print(f"Addition: {x} + {y} = {x + y}")
print(f"Subtraction: {x} - {y} = {x - y}")
print(f"Multiplication: {x} * {y} = {x * y}")
print(f"Division: {x} / {y} = {x / y}")
print(f"Integer Division: {x} // {y} = {x // y}")
print(f"Modulo: {x} % {y} = {x % y}")
print(f"Power: {x} ** {y} = {x ** y}")

# Booleans
print("\n=== Working with Booleans ===")
is_sunny = True
is_raining = False
print(f"Is sunny: {is_sunny}")
print(f"Is raining: {is_raining}")
print(f"Is sunny AND raining: {is_sunny and is_raining}")
print(f"Is sunny OR raining: {is_sunny or is_raining}")
print(f"NOT sunny: {not is_sunny}")