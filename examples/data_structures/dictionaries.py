"""
Python Data Structures: Dictionaries

This file demonstrates working with dictionaries in Python.
"""

# Creating Dictionaries
print("=== Creating Dictionaries ===")
# Empty dictionary
empty_dict = {}
print(f"Empty dictionary: {empty_dict}")

# Dictionary with items
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "job": "Engineer"
}
print(f"Person: {person}")

# Dictionary with different data types
mixed_dict = {
    "string": "hello",
    "number": 42,
    "list": [1, 2, 3],
    "boolean": True
}
print(f"Mixed dictionary: {mixed_dict}")

# Accessing Dictionary Elements
print("\n=== Accessing Elements ===")
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")

# Using get() method (safer)
print(f"City: {person.get('city')}")
print(f"Country: {person.get('country', 'Not specified')}")  # Default value

# Modifying Dictionaries
print("\n=== Modifying Dictionaries ===")
person["age"] = 31  # Update existing key
print(f"Updated age: {person}")

person["country"] = "USA"  # Add new key
print(f"Added country: {person}")

del person["job"]  # Remove key
print(f"Removed job: {person}")

# Dictionary Methods
print("\n=== Dictionary Methods ===")
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")
print(f"Items: {list(person.items())}")

# Check if key exists
print(f"'name' in person: {'name' in person}")
print(f"'job' in person: {'job' in person}")

# Copy dictionary
person_copy = person.copy()
print(f"Copy: {person_copy}")

# Working with Dictionary Items
print("\n=== Looping Through Dictionaries ===")
# Loop through keys
print("Keys:")
for key in person:
    print(f"  {key}")

# Loop through values
print("Values:")
for value in person.values():
    print(f"  {value}")

# Loop through key-value pairs
print("Key-Value pairs:")
for key, value in person.items():
    print(f"  {key}: {value}")

# Dictionary Comprehensions
print("\n=== Dictionary Comprehensions ===")
# Create dictionary from lists
keys = ["a", "b", "c", "d"]
values = [1, 2, 3, 4]
letter_numbers = {k: v for k, v in zip(keys, values)}
print(f"Letter numbers: {letter_numbers}")

# Create dictionary with condition
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Nested Dictionaries
print("\n=== Nested Dictionaries ===")
students = {
    "student1": {
        "name": "Alice",
        "grades": [85, 90, 78]
    },
    "student2": {
        "name": "Bob",
        "grades": [92, 88, 95]
    }
}

print(f"Students: {students}")
print(f"Alice's grades: {students['student1']['grades']}")

# Common Dictionary Operations
print("\n=== Common Operations ===")
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 96}
print(f"Scores: {scores}")
print(f"Number of students: {len(scores)}")
print(f"Highest score: {max(scores.values())}")
print(f"Lowest score: {min(scores.values())}")
print(f"Average score: {sum(scores.values()) / len(scores):.1f}")

# Find student with highest score
top_student = max(scores, key=scores.get)
print(f"Top student: {top_student} with score {scores[top_student]}")