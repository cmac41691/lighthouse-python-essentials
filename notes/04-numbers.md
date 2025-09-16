# Chapter 3: Numbers  
## Lesson: Introduction to Numbers  
**Date**: 2025-09-16  

---

### 📝 Key Ideas
- A **number** is not a string. We cannot do string operations (like `len()` or concatenation) on numbers.  
- Example:  
  ```python
  len(1)          # ❌ TypeError: object of type 'int' has no len()
  "milkshake " + 2  # ❌ TypeError: must be str, not int
2 + 2      # ✅ 4
"2" + "2"  # ✅ '22'
"2" + 2    # ❌ TypeError


"2" + 2  
# ❌ TypeError: must be str, not int

## Integers and Floats
- Integers (`int`): whole numbers, positive or negative (e.g., 10, -7, 600001)  
- Floats (`float`): numbers with decimals (e.g., 3.14, 806.63, 1.0)  

## Type Conversion
# Use float() to convert an integer into a float:
float(2)   # 2.0

# Use int() to convert a float into an integer (decimal part is chopped, not rounded):
int(2.0)   # 2
int(2.5)   # 2   # chopped, not rounded

## Summary
- Strings and numbers look similar but behave differently.

- Python distinguishes between int and float.

- Type conversion functions int() and float() are useful for switching between them.

- Important: converting floats to integers drops decimals instead of rounding