# Exercise 20: Cube Numbers
"""
Returns a new list containing the cubes of all numbers in the given list.

Example:
    cube_numbers([1, 2, 3]) -> [1, 8, 27]
    cube_numbers([-1, 0, 2]) -> [-1, 0, 8]
"""
def cube_numbers(numbers: list):
    new_numbers = []

    for i in range(len(numbers)):
        new_numbers.append(numbers[i] ** 3)

    return new_numbers

print(cube_numbers([1, 2, 3]))

# Exercise 21: Count Consonants
"""
Returns the number of consonants in a string.
Ignore spaces and capitalization.

Example:
    count_consonants("hello") -> 3
    count_consonants("Python") -> 5
"""
def count_consonants(s: str):
    s = s.lower()
    vowels = "aeiou"
    consonants = 0

    for i in range(len(s)):
        if s[i].isalpha() and s[i] not in vowels:  # check if it's a consonant
            consonants += 1

    return consonants

print(count_consonants("hello"))  # -> 3
print(count_consonants("Python")) # -> 5

# Exercise 22: Shortest Word
"""
Returns the shortest word in a given sentence.
If there are multiple words with the same length, return the first one.

Example:
    find_shortest_word("Python is awesome") -> "is"
    find_shortest_word("I love AI") -> "I"
"""
def find_shortest_word(sentence: str):
    words = sentence.strip()
    shortest_word = ""

    for i in range(len(words)):
        if len(words[i]) > len(shortest_word):
            shortest_word = sentence[i]
    return shortest_word

print(find_shortest_word("Python is awesome"))
print(find_shortest_word("I love AI"))

# Exercise 23: Reverse Words in Sentence
"""
Reverses the order of words in a sentence.

Example:
    reverse_sentence("Python is fun") -> "fun is Python"
    reverse_sentence("Hello world") -> "world Hello"
"""
"""
✅ Key points

• Extra parentheses cause syntax errors.

- Do not mix characters and numeric ranges in if.

- split() + join() is the easiest and most Pythonic way to reverse words.

- Use range(len(...)-1, -1, -1) for index-based reverse iteration.
"""
def reverse_sentence(sentence: str):
    words = sentence.split()
    reversed_words = []

    for i in range(len(words)-1, -1, -1):
        reversed_words.append(words[i])

    return " ".join(reversed_words)

print(reverse_sentence("Python is fun"))
print(reverse_sentence("Hello world"))

# Exercise 24: Unique Elements
"""
Returns a new list containing only the unique elements from a list.
Order does not matter here.

Example:
    unique_elements([1, 2, 2, 3, 1]) -> [1, 2, 3]
    unique_elements(["a", "b", "a"]) -> ["a", "b"]
"""
def unique_elements(items: list):
    new_elements =[]

    for i in range(len(items)):
        if items[i] not in new_elements:
            new_elements.append(items[i])

    return new_elements

print(unique_elements([1, 2, 2, 3, 1]))
print(unique_elements(["a", "b", "a"]))

# Exercise 25: Movie Class
"""
Represents a movie with title, director, and release year.

Attributes:
    title (str): Movie title
    director (str): Movie director
    year (int): Release year

Methods:
    summary() -> Returns "'{title}' directed by {director}, released in {year}."

Example:
    m = Movie("Inception", "Christopher Nolan", 2010)
    m.summary() -> "'Inception' directed by Christopher Nolan, released in 2010."
"""
class Movie:
    def __init__(self, title: str, director: str, year: int):
        self.title = title
        self.director = director
        self.year = year

    def summary(self):
        return f"'{self.title}' directed by {self.director}, released in {self.year}."
    
m = Movie("Inception", "Christopher Nolan", 2010)
print(m.summary())

# Exercise 26: Grade Converter
"""
Converts a numerical grade into a letter grade.
Use the following scale:
    90-100 -> 'A'
    80-89  -> 'B'
    70-79  -> 'C'
    60-69  -> 'D'
    0-59   -> 'F'

Example:
    grade_converter(95) -> 'A'
    grade_converter(72) -> 'C'
"""
def grade_converter(grade: int):
    if grade in range(90, 101):
        return 'A'
    elif grade in range(80, 90):
        return 'B'
    elif grade in range(70, 80):
        return 'C'
    elif grade in range(60, 70):
        return 'D'
    elif grade in range(0, 60):
        return 'F'

print(grade_converter(95))
print(grade_converter(72))
