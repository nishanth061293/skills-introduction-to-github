"""
Python Data Structures: Lists

This file demonstrates working with lists in Python.
"""

# Creating Lists
print("=== Creating Lists ===")
# Empty list
empty_list = []
print(f"Empty list: {empty_list}")

# List with items
fruits = ["apple", "banana", "orange", "grape"]
print(f"Fruits: {fruits}")

# List with different data types
mixed_list = [1, "hello", 3.14, True]
print(f"Mixed list: {mixed_list}")

# List with numbers
numbers = [1, 2, 3, 4, 5]
print(f"Numbers: {numbers}")

# Accessing List Elements
print("\n=== Accessing Elements ===")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Second to last: {fruits[-2]}")

# List Slicing
print("\n=== List Slicing ===")
print(f"First two fruits: {fruits[0:2]}")
print(f"From second to end: {fruits[1:]}")
print(f"All except last: {fruits[:-1]}")
print(f"Every other fruit: {fruits[::2]}")

# Modifying Lists
print("\n=== Modifying Lists ===")
fruits.append("kiwi")  # Add to end
print(f"After append: {fruits}")

fruits.insert(1, "mango")  # Insert at position
print(f"After insert: {fruits}")

fruits.remove("banana")  # Remove specific item
print(f"After remove: {fruits}")

removed_fruit = fruits.pop()  # Remove and return last item
print(f"Popped: {removed_fruit}, List: {fruits}")

fruits[0] = "pineapple"  # Change specific item
print(f"After changing first item: {fruits}")

# List Methods
print("\n=== List Methods ===")
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(f"Original numbers: {numbers}")

numbers.sort()  # Sort in place
print(f"After sort: {numbers}")

numbers.reverse()  # Reverse in place
print(f"After reverse: {numbers}")

print(f"Count of 5: {numbers.count(5)}")
print(f"Index of 4: {numbers.index(4)}")

# List Comprehensions
print("\n=== List Comprehensions ===")
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even numbers 1-10: {even_numbers}")

# Working with Multiple Lists
print("\n=== Working with Multiple Lists ===")
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation
combined = list1 + list2
print(f"Combined: {combined}")

# Zip function
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
paired = list(zip(names, ages))
print(f"Paired: {paired}")

# Common List Operations
print("\n=== Common Operations ===")
numbers = [1, 2, 3, 4, 5]
print(f"Length: {len(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Min: {min(numbers)}")
print(f"Check if 3 is in list: {3 in numbers}")
print(f"Check if 10 is in list: {10 in numbers}")