# Python Exercises – Indexing Cheat Sheet
## 1️⃣ Multiply Numbers

**Element-based:**
```python
def multiply_numbers(a, b):
    return a * b
```

- Indexing doesn’t apply here (single values, not a list).
## 2️⃣ Divide Numbers

**Element-based:**
```python
def divide_numbers(a, b):
    if b == 0:
        return None
    return a / b
```

- Indexing not needed (single values).
## 3️⃣ Reverse String

**Element-based:**
```python
def reverse_string(s: str):
    return s[::-1]
```

- Index-based version:
```python
def reverse_string(s: str):
    reversed_s = ""
    for i in range(len(s)-1, -1, -1):
        reversed_s += s[i]
    return reversed_s
```

## 4️⃣ Count Vowels

**Element-based:**
```python
def count_vowels(s: str):
    count = 0
    vowels = "aeiou"
    for char in s.lower():
        if char in vowels:
            count += 1
    return count
```

- Index-based version:
```python
def count_vowels(s: str):
    count = 0
    vowels = "aeiou"
    s = s.lower()
    for i in range(len(s)):
        if s[i] in vowels:
            count += 1
    return count
```

## 5️⃣ Sum List

**Element-based:**
```python
def sum_list(numbers: list):
    total = 0
    for num in numbers:
        total += num
    return total
```

- Index-based version:
```python
def sum_list(numbers: list):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total
```

## 6️⃣ Count Even Numbers

**Element-based:**
```python
def count_even(numbers: list):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count
```

- Index-based version:
```python
def count_even(numbers: list):
    count = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            count += 1
    return count
```

## 7️⃣ Count Odd Numbers

**Element-based:**
```python
def count_odd(numbers: list):
    count = 0
    for num in numbers:
        if num % 2 != 0:
            count += 1
    return count
```

- Index-based version:
```python
def count_odd(numbers: list):
    count = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 != 0:
            count += 1
    return count
```

## 8️⃣ Find Minimum and Maximum

**Element-based:**
```python
def find_min_max(numbers: list):
    if not numbers:
        return None
    return (min(numbers), max(numbers))
```

-Index-based version:
```python
def find_min_max(numbers: list):
    if not numbers:
        return None
    min_val = numbers[0]
    max_val = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < min_val:
            min_val = numbers[i]
        if numbers[i] > max_val:
            max_val = numbers[i]
    return (min_val, max_val)
```

## 9️⃣ Remove Duplicates

**Element-based:**
```python
def remove_duplicates(items: list):
    new_list = []
    for item in items:
        if item not in new_list:
            new_list.append(item)
    return new_list
```

- Index-based version:
```python
def remove_duplicates(items: list):
    new_list = []
    for i in range(len(items)):
        if items[i] not in new_list:
            new_list.append(items[i])
    return new_list
```

## 🔟 Find Longest Word

**Element-based:**
```python
def find_longest_word(sentence: str):
    words = sentence.split()
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word
```

- Index-based version:
```python
def find_longest_word(sentence: str):
    words = sentence.split()
    longest_word = ""
    for i in range(len(words)):
        if len(words[i]) > len(longest_word):
            longest_word = words[i]
    return longest_word
```

## ✅ Key Takeaways from the Cheat Sheet

**Use for i in range(len(list)) when:**

- You need the position of elements.

- You want to modify the list in place.

- You want full control over indexing operations.

- Use for item in list when:

- You just need the element value.

- You don’t need the index.

- Cleaner, simpler, and more Pythonic for most cases.

- Strings can be treated as lists of characters in indexing.

- Indexing is a universal skill — useful for lists, strings, and even nested lists.
