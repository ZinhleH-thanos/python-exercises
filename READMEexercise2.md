# 🐍 Beginner Python Exercises – Quick Reference Cheat Sheet
🔹 find_min_max(numbers)

- Use min() and max() to get smallest/largest.

- Check for empty list with if not numbers:

- Return both as a tuple → (min, max)

🔹 count_odd(numbers)

- Use % to test odd numbers → num % 2 != 0

- Initialize a counter → count = 0

- Loop and increment when condition is true.

🔹 is_palindrome(s)

- Convert to lowercase → .lower()

- Remove spaces → .replace(" ", "")

- Compare with reverse → s == s[::-1]

🔹 factorial(n)

- Handle base case → if n == 0: return 1

- Multiply from 1 to n in a loop.

- Keep a running result → result *= i

🔹 Student class

- __init__ sets up self.name and self.grades

- .average() → sum(self.grades) / len(self.grades)

- .greet() → return f"Hello, my name is {self.name}"

## 🧩 General Tips

- Always read docstrings carefully (they tell you input/output).

- Identify task type → math, string, list, or class.

- Handle edge cases (empty lists, 0 division, etc.).

- Test with example inputs after writing each function.
