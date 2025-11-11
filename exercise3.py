# Exercise 14: Square Numbers
"""
Returns a new list containing the squares of all numbers in the given list.

Example:
    square_numbers([1, 2, 3]) -> [1, 4, 9]
    square_numbers([-1, 0, 2]) -> [1, 0, 4]
"""
def square_numbers(numbers: list):
    new_square = []

    for i in range(len(numbers)):
        new_square.append(numbers[i] * numbers[i])

    return new_square

print(square_numbers([1, 2, 3]))  # -> [1, 4, 9]

# Exercise 15: Count Words
"""
Returns the number of words in a given sentence.
A word is defined as any sequence of characters separated by spaces.

Example:
    count_words("Hello world") -> 2
    count_words("Python is fun") -> 3
"""
def count_words(sentence: str):
    sentence = sentence.lower()
    words = sentence.split()   # Split the sentence into a list of words
    num_of_words = 0

    for word in words: 
        if word in words:        # Loop through each word in the list
            num_of_words = num_of_words + 1

    return num_of_words

print(count_words("Hello world"))       # -> 2
print(count_words("Python is fun"))

# Exercise 16: Find Longest Word
"""
Returns the longest word in a given sentence.
If there are multiple words of the same length, return the first one.

Example:
    find_longest_word("Python is awesome") -> "awesome"
    find_longest_word("I love AI") -> "love"
"""
def find_longest_word(sentence: str):
    words = sentence.split()
    longest_word = ""
    for i in range(len(words)):
        if len(words[i]) > len(longest_word):
            longest_word = words[i]
    return longest_word

print(find_longest_word("Python is awesome"))
# Exercise 17: Temperature Converter
"""
Converts temperature between Celsius and Fahrenheit.

Arguments:
    temp (float): The temperature value
    scale (str): Target scale - 'C' for Celsius or 'F' for Fahrenheit

Example:
    convert_temp(0, 'F') -> 32.0
    convert_temp(212, 'C') -> 100.0
"""
def convert_temp(temp: float, scale: str):
    pass


# Exercise 18: Remove Duplicates
"""
Removes duplicate values from a list while preserving the original order.

Example:
    remove_duplicates([1, 2, 2, 3, 1]) -> [1, 2, 3]
    remove_duplicates(["a", "b", "a"]) -> ["a", "b"]
"""
def remove_duplicates(items: list):
    new_list = []

    for i in range(len(items)):      # i is the index
        if items[i] not in new_list: # check the element at index i
            new_list.append(items[i])

    return new_list

print(remove_duplicates([1, 2, 2, 3, 1]))   # -> [1, 2, 3]
print(remove_duplicates(["a", "b", "a"]))   # -> ["a", "b"]


# Exercise 19: Book Class
"""
Represents a book with title, author, and number of pages.

Attributes:
    title (str): Title of the book
    author (str): Author of the book
    pages (int): Number of pages in the book

Methods:
    description() -> Returns "'{title}' by {author}, {pages} pages."

Example:
    b = Book("1984", "George Orwell", 328)
    b.description() -> "'1984' by George Orwell, 328 pages."
"""
class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def description(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"
    
b = Book("1984", "George Orwell", 328)
print(b.description())
