# String Sum Kata

A programming kata that creates a utility to sum two string numbers, handling invalid inputs by replacing them with zero.

## Rules

Write a simple String Sum utility with a function `stringSum(string num1, string num2)` that:

- Accepts only natural numbers (non-negative integers)
- Returns their sum
- Replaces any invalid input with 0 (zero)
- Handles empty strings, non-numeric strings, and negative numbers

## Example Output

```
stringSum("123", "456") → 579
stringSum("123", "abc") → 123
stringSum("", "456") → 456
stringSum("-5", "10") → 10
stringSum("abc", "def") → 0
```

## Run

```bash
python src/stringsum.py
```

## Test

```bash
pytest src/test_stringsum.py -v
```