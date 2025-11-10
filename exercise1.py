# beginner-python-exercises: Beginner Exercises
# --------------------------------------------
# Complete the following functions and class according to the instructions.

# Exercise 1: Multiply Numbers
"""
Returns the product of two numbers.

Example:
    multiply_numbers(2, 3) -> 6
    multiply_numbers(-1, 4) -> -4
"""
def multiply_numbers(a, b):
    result = a * b
    return result

print(multiply_numbers(2, 3))

# Exercise 2: Divide Numbers
"""
Returns the result of a divided by b.
If b is 0, return None.

Example:
    divide_numbers(6, 3) -> 2
    divide_numbers(5, 0) -> None
"""
def divide_numbers(a, b):
    if b == 0: # WE CANNOT DIVIDE BY 0, HENCE B == 0 RETURNS NONE
        return None
    else:
        result = a / b
    return result

print(divide_numbers(6, 3))

# Exercise 3: Reverse String
"""
Returns the reverse of the given string.

Example:
    reverse_string("hello") -> "olleh"
    reverse_string("Python") -> "nohtyP"
"""
def reverse_string(s: str):
    s = s[::-1]
    return s # RETURN THE WHOLE STRING
    
print(reverse_string("hello"))
    
# Exercise 4: Count Vowels
"""
Returns the number of vowels in a string.

Example:
    count_vowels("hello") -> 2
    count_vowels("Python") -> 1
"""
def count_vowels(s: str):
    s = s.lower()
    vowels = "aeiou"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


print(count_vowels("hello"))

# Exercise 5: Sum List
"""
Returns the sum of all numbers in a list.

Example:
    sum_list([1,2,3]) -> 6
    sum_list([-1,-5,-3]) -> -9
"""
def sum_list(numbers: list):
    result = sum(numbers)
    return result

print(sum_list([1,2,3]))

# Exercise 6: Count Even Numbers
"""
Returns the number of even numbers in a list.

Example:
    count_even([1,2,3,4]) -> 2
    count_even([1,3,5]) -> 0
"""
def count_even(numbers: list):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count = count + 1 
    return count

print(count_even([1,2,3,4]))

# Exercise 7: Car Class
"""
Represents a car with make, model, and year.

Attributes:
    make (str): Car brand
    model (str): Car model
    year (int): Year of manufacture

Method:
    description() -> "This car is a {year} {make} {model}."

Example:
    c = Car("Toyota", "Corolla", 2020)
    c.description() -> "This car is a 2020 Toyota Corolla."
"""
class Car:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"This car is a {self.year} {self.make} {self.model}"
    
c = Car("Toyota", "Corolla", 2020)
print(c.description())
