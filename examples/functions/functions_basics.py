"""
Python Functions

This file demonstrates how to create and use functions in Python.
"""

# Basic Function
def greet(name):
    """A simple function that greets someone."""
    return f"Hello, {name}!"

# Function with Default Parameters
def greet_with_title(name, title="Mr./Ms."):
    """Greet someone with a title."""
    return f"Hello, {title} {name}!"

# Function with Multiple Parameters
def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

# Function with Multiple Return Values
def get_name_parts(full_name):
    """Split a full name into first and last name."""
    parts = full_name.split()
    first_name = parts[0]
    last_name = parts[-1] if len(parts) > 1 else ""
    return first_name, last_name

# Function with Variable Arguments
def calculate_average(*numbers):
    """Calculate the average of any number of arguments."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Function with Keyword Arguments
def create_profile(**kwargs):
    """Create a user profile from keyword arguments."""
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    return profile

# Main execution
if __name__ == "__main__":
    print("=== Function Examples ===")
    
    # Basic function
    message = greet("Alice")
    print(message)
    
    # Function with default parameter
    print(greet_with_title("Bob"))
    print(greet_with_title("Charlie", "Dr."))
    
    # Function with multiple parameters
    result = add_numbers(5, 3)
    print(f"5 + 3 = {result}")
    
    # Function with multiple return values
    first, last = get_name_parts("John Doe")
    print(f"First name: {first}, Last name: {last}")
    
    # Function with variable arguments
    avg1 = calculate_average(1, 2, 3, 4, 5)
    avg2 = calculate_average(10, 20)
    print(f"Average of 1,2,3,4,5: {avg1}")
    print(f"Average of 10,20: {avg2}")
    
    # Function with keyword arguments
    user = create_profile(name="Alice", age=30, city="New York", job="Engineer")
    print(f"User profile: {user}")

# Lambda Functions (Anonymous Functions)
print("\n=== Lambda Functions ===")
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"Original: {numbers}")
print(f"Squared: {squared_numbers}")

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")