
## Lesson: Introduction to Numbers  
# Chapter 3: Numbers  

---

## Lesson: Introduction to Numbers  
**Date**: 2025-09-16  

### 📝 Key Ideas  
- A **number** is not a string.  
- String operations (`len()`, concatenation) cannot be applied to numbers.  

#### Examples  
```python
len(1)            # ❌ TypeError: object of type 'int' has no len()
"milkshake " + 2  # ❌ TypeError: must be str, not int

2 + 2       # ✅ 4
"2" + "2"   # ✅ '22'
"2" + 2     # ❌ TypeError



"2" + 2  
# ❌ TypeError: must be str, not int

## Integers and Floats
- Integers (`int`): whole numbers, positive or negative (e.g., 10, -7, 600001)  
- Floats (`float`): numbers with decimals (e.g., 3.14, 806.63, 1.0)  

## Type Conversion
# Use float() to convert an integer into a float:
# Convert int → float
float(2)    # 2.0

# Convert float → int (decimal part is chopped, not rounded)
int(2.0)    # 2
int(2.5)    # 2

## Summary
- Strings and numbers look similar but behave differently.
- Python distinguishes between int and float.
- Type conversion functions int() and float() are useful for switching between them.
- Important: converting floats to integers drops decimals instead of rounding

## Lesson: Math in Python  
**Date**: 2025-09-20  

---

### 📝 Key Ideas  
- Python can perform all basic math operations: addition, subtraction, multiplication, division, and more.  
- Variables can store numbers and be used directly in expressions.  
- Python also supports exponentiation and compound calculations.  

---

### 🔢 Basic Operations  
```python
a = 14
b = 5

# Addition
a + b   # 19

# Subtraction
a - b   # 9

# Multiplication
a * b   # 70

# Division
a / b   # 2.8

### Exponentiation and Compound Expressions

# Exponentiation (a to the power of b)
a ** b   # 14^5

# Compound calculation
c = 8
a + b * c ** a


### Notes
- Use print() to see results in the console — just writing the expression won’t output anything.

- Expressions don’t have to be assigned to a variable, but they can be.

- Python has a math library for advanced operations (e.g., square root, sine, factorial).

## Comparing Numbers (Comparison Operators)
a = 14
b = 5

a == b   # False   | Equals
a != b   # True    | Doesn't equal
a > b    # True    | Greater than
a >= b   # True    | Greater than or equal to
a < b    # False   | Less than
a <= b   # False   | Less than or equal to


- These expressions evaluate to a Boolean → either True or False.

📖 Summary

Python handles math with familiar operators (+, -, *, /, **).

You can compare numbers with comparison operators (==, !=, >, <, >=, <=).

Results of comparisons are Booleans (True or False).

The math library unlocks more advanced functions when needed.