#!/usr/bin/env python3

def greet_programmer():
    """This function prints a greeting to the programmer."""
    print("Hello, programmer!")

def greet(name):
    """This function prints a greeting to a specified person."""
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    """This function prints a greeting to a specified person, or to 'programmer' if no name is given."""
    print(f"Hello, {name}!")

def add(num1, num2):
    """This function returns the sum of two numbers."""
    return num1 + num2

def halve(number):
    """This function returns half of the given number."""
    return number / 2

# Test the functions to verify they work as expected
if __name__ == "__main__":
    greet_programmer()  # Should print: Hello, programmer!

    greet("Alice")  # Should print: Hello, Alice!

    greet_with_default()  # Should print: Hello, programmer!
    greet_with_default("Bob")  # Should print: Hello, Bob!

    print(add(3, 4))  # Should print: 7

    print(halve(10))  # Should print: 5.0
