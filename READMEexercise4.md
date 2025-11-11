## 🌟 1. Loops + Indexing Power

**You consistently used:**
```python
for i in range(len(items)):
```

• That’s your preferred indexing style — and you used it perfectly to:

• Access each element by position

• Compare or modify items

• Append to new lists

- ✅ This reinforces control over how loops step through data.


## 🧮 2. List Building Patterns

**You created new lists step by step — great for clean logic:**
```python
new_numbers = []
for i in range(len(numbers)):
    new_numbers.append(numbers[i] ** 3)
```

- That’s clear, safe, and easy to debug.


## 🔡 3. String Manipulation (Lowercase, Split, Join)

**You nailed some essential string techniques:**

• .lower() → normalize letters

• .split() → break a sentence into words

• " ".join(list) → rebuild a sentence

- Those three are some of the most used string tools in Python.
- They’re the foundation for text processing.

##🧩 4. Logical Thinking in Conditions

**You wrote:**
```python
if grade in range(90, 101):
    return 'A'
```

## ✅ You correctly fixed the off-by-one issues (range upper limit is exclusive).
## ✅ You used elif cleanly — that’s good control flow practice.


## 🔤 5. Class Basics: Attributes + Methods

**Your Movie class:**
```python
class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def summary(self):
        return f"'{self.title}' directed by {self.director}, released in {self.year}."
```

## ✅ Perfect syntax
## ✅ Clear method
## ✅ f-string use is spot on
-This shows you understand object construction, instance attributes, and methods that return strings.

## 🔁 6. Deduplication Logic

**Your unique_elements() is excellent:**
```python
if items[i] not in new_elements:
    new_elements.append(items[i])
```
- That’s how we keep order while removing duplicates — much better than using set() if order matters.

## ⚙️ 7. Debugging Mindset

• You caught earlier issues like:

• Using range incorrectly with characters

• Mixing print and return

• Parentheses mismatches
