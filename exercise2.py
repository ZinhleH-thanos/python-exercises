# Exercise 9: Find Minimum and Maximum
"""
Returns a tuple containing the smallest and largest numbers in a list.
If the list is empty, return None.

Example:
    find_min_max([1, 2, 3, 4]) -> (1, 4)
    find_min_max([10, -5, 7]) -> (-5, 10)
    find_min_max([]) -> None
"""
def find_min_max(numbers: list):
    if not numbers:
        return None
    return(min(numbers), max(numbers))

print(find_min_max([10, -5, 7]))

# Exercise 10: Count Odd Numbers
"""
Returns the number of odd numbers in a list.

Example:
    count_odd([1, 2, 3, 4, 5]) -> 3
    count_odd([2, 4, 6]) -> 0
"""
def count_odd(numbers: list):
    count = 0

    for num in numbers:
        if num % 2 != 0:
            count = count + 1
    return count

print(count_odd([1, 2, 3, 4, 5]))

# Exercise 11: Palindrome Checker
"""
Returns True if the given string is a palindrome, False otherwise.
Ignore spaces and capitalization.

Example:
    is_palindrome("racecar") -> True
    is_palindrome("Hello") -> False
    is_palindrome("A man a plan a canal Panama") -> True
"""
def is_palindrome(s: str):
    s = s.lower().replace(" ", "")

    return s == s[::-1]

print(is_palindrome("racecar"))

# Exercise 12: Factorial
"""
Returns the factorial of a given non-negative integer n.
The factorial of 0 is 1.

Example:
    factorial(5) -> 120
    factorial(0) -> 1
"""
def factorial(n: int):
    # Base case:
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

    # Exercise 13: Student Class
"""
Represents a student with a name and a list of grades.

Attributes:
    name (str): Name of the student
    grades (list of numbers): Grades the student received

Methods:
    average() -> Returns the average of the grades
    greet() -> Returns "Hello, my name is {name}."

Example:
    s = Student("Alice", [80, 90, 100])
    s.average() -> 90.0
    s.greet() -> "Hello, my name is Alice."
"""
class Student:
    def __init__(self, name: str, grades: list):
        self.name = name
        self.grades = grades

    def average(self):
        average = sum(self.grades)/len(self.grades)
        return average

    def greet(self):
        return f"Hello, my name is {self.name}"
    
s = Student("Alice", [80, 90, 100])
print(s.average())
print(s.greet())
