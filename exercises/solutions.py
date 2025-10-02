"""
Solutions to Python Practice Exercises - Beginner Level

Here are the solutions to the exercises. Try to solve them yourself first!
"""

print("=== Exercise 1: Basic Calculations ===")
# Create variables for your age and the current year
# Calculate and print what year you were born

age = 25
current_year = 2024
birth_year = current_year - age
print(f"I was born in {birth_year}")


print("\n=== Exercise 2: String Manipulation ===")
# Create a variable with your full name
# Print your name in uppercase, lowercase, and title case
# Count and print the number of characters in your name

full_name = "John Doe"
print(f"Uppercase: {full_name.upper()}")
print(f"Lowercase: {full_name.lower()}")
print(f"Title case: {full_name.title()}")
print(f"Number of characters: {len(full_name)}")


print("\n=== Exercise 3: Lists Practice ===")
# Create a list of your 5 favorite foods
# Add a new food to the list
# Remove one food from the list
# Print the final list and its length

favorite_foods = ["pizza", "sushi", "tacos", "ice cream", "pasta"]
print(f"Original list: {favorite_foods}")

favorite_foods.append("chocolate")
print(f"After adding chocolate: {favorite_foods}")

favorite_foods.remove("tacos")
print(f"After removing tacos: {favorite_foods}")
print(f"Final list length: {len(favorite_foods)}")


print("\n=== Exercise 4: Temperature Converter ===")
# Write a function that converts Celsius to Fahrenheit
# Formula: F = (C * 9/5) + 32

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Test the function
print(f"0°C = {celsius_to_fahrenheit(0)}°F")
print(f"25°C = {celsius_to_fahrenheit(25)}°F")
print(f"100°C = {celsius_to_fahrenheit(100)}°F")


print("\n=== Exercise 5: Even or Odd ===")
# Write a function that checks if a number is even or odd

def even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

# Test the function
print(f"4 is {even_or_odd(4)}")
print(f"7 is {even_or_odd(7)}")
print(f"10 is {even_or_odd(10)}")


print("\n=== Exercise 6: Count Vowels ===")
# Write a function that counts the number of vowels in a string

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Alternative solution using list comprehension
def count_vowels_v2(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

# Test the function
print(f"Vowels in 'hello': {count_vowels('hello')}")
print(f"Vowels in 'Python': {count_vowels('Python')}")
print(f"Vowels in 'Programming': {count_vowels('Programming')}")


print("\n=== Exercise 7: Shopping List ===")
# Create a dictionary representing a shopping list
# Add a function to calculate the total number of items

shopping_list = {
    "apples": 6,
    "bread": 2,
    "milk": 1,
    "eggs": 12,
    "cheese": 1
}

def total_items(shopping_dict):
    return sum(shopping_dict.values())

# Test the function
print(f"Shopping list: {shopping_list}")
print(f"Total items: {total_items(shopping_list)}")


print("\n=== Exercise 8: Number Guessing Game ===")
# Create a simple number guessing game

import random

def number_guessing_game():
    # Computer picks a random number between 1 and 10
    secret_number = random.randint(1, 10)
    guesses_left = 3
    
    print("I'm thinking of a number between 1 and 10!")
    print(f"You have {guesses_left} guesses.")
    
    while guesses_left > 0:
        try:
            guess = int(input("Enter your guess: "))
            
            if guess == secret_number:
                print(f"Congratulations! You guessed it! The number was {secret_number}")
                return
            elif guess < secret_number:
                print("Too low!")
            else:
                print("Too high!")
            
            guesses_left -= 1
            if guesses_left > 0:
                print(f"You have {guesses_left} guesses left.")
        
        except ValueError:
            print("Please enter a valid number!")
    
    print(f"Game over! The number was {secret_number}")

# Uncomment to play the game:
# number_guessing_game()


print("\n=== Bonus Exercise: Word Counter ===")
# Write a function that counts how many times each word appears in a sentence

def count_words(sentence):
    # Convert to lowercase and remove punctuation
    import string
    
    # Remove punctuation and convert to lowercase
    cleaned = sentence.lower()
    for char in string.punctuation:
        cleaned = cleaned.replace(char, "")
    
    # Split into words
    words = cleaned.split()
    
    # Count words
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

# Alternative solution using Counter from collections
from collections import Counter
import string

def count_words_v2(sentence):
    # Remove punctuation and convert to lowercase
    cleaned = sentence.lower()
    for char in string.punctuation:
        cleaned = cleaned.replace(char, "")
    
    words = cleaned.split()
    return dict(Counter(words))

# Test the function
text = "The quick brown fox jumps over the lazy dog. The dog was really lazy."
word_count = count_words(text)
print(f"Word count: {word_count}")

print("\nCongratulations! You've completed all the Python exercises!")
print("Keep practicing to improve your programming skills!")