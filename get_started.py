#!/usr/bin/env python3
"""
Python Learning Repository - Getting Started Script

This script helps you get started with the Python examples.
Run this script to see all available examples and exercises.
"""

import os
import sys

def print_banner():
    print("=" * 60)
    print("🐍 Welcome to Python Learning Repository! 🐍")
    print("=" * 60)
    print()

def list_examples():
    print("📚 Available Examples:")
    print()
    
    examples_dir = "examples"
    if os.path.exists(examples_dir):
        for root, dirs, files in os.walk(examples_dir):
            for file in files:
                if file.endswith('.py'):
                    filepath = os.path.join(root, file)
                    print(f"  📄 {filepath}")
    print()

def list_exercises():
    print("💪 Available Exercises:")
    print()
    
    exercises_dir = "exercises"
    if os.path.exists(exercises_dir):
        for file in os.listdir(exercises_dir):
            if file.endswith('.py'):
                filepath = os.path.join(exercises_dir, file)
                print(f"  📝 {filepath}")
    print()

def run_example(filepath):
    """Run a Python example file."""
    print(f"\n🚀 Running {filepath}...")
    print("-" * 50)
    try:
        # Import and execute the file
        exec(open(filepath).read())
        print("-" * 50)
        print(f"✅ {filepath} completed successfully!")
    except Exception as e:
        print(f"❌ Error running {filepath}: {e}")
    print()

def main():
    print_banner()
    
    print("This repository contains Python examples and exercises to help you learn.")
    print("Here's what's available:")
    print()
    
    list_examples()
    list_exercises()
    
    print("🎯 Getting Started:")
    print("1. Start with examples/basics/01_variables_and_types.py")
    print("2. Move through the examples in order")
    print("3. Try the exercises to practice what you've learned")
    print("4. Experiment with the code - modify and run it!")
    print()
    
    print("🔧 How to run examples:")
    print("   python3 examples/basics/01_variables_and_types.py")
    print("   python3 examples/functions/functions_basics.py")
    print("   python3 exercises/beginner_exercises.py")
    print()
    
    # Ask if user wants to run a demo
    try:
        choice = input("Would you like to run a quick demo? (y/n): ").lower().strip()
        if choice in ['y', 'yes']:
            print("\n🎬 Running demo - Variables and Types example:")
            run_example("examples/basics/01_variables_and_types.py")
    except KeyboardInterrupt:
        print("\n\n👋 Happy coding!")
    except:
        print("\n📖 Check out the examples when you're ready!")

if __name__ == "__main__":
    main()