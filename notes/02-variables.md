
### `notes/02-variables.md`
```markdown
# Variables

## Key ideas (in my words)
- Variables store values (text, numbers, lists).
- Use comments to explain intent.

## Example
```python
# name is a string; tax/subtotal/total are numbers
name = "Thomas"
tax_rate = 0.14
subtotal = 20
tax = subtotal * tax_rate
total = subtotal + tax
print(f"Hello, {name}. Your total is {total}.")

## Step-by-step recipe
1.Declare variables with clear names
2.Do calculations in small steps
3.Print/format the result to verify

## Mini challenge idea
- Prompt for a trip budget (flight, hotel, food), apply tax, print total.

## Tricky parts to revisit
 -f strings vs concatenation
 - Float rounding (e.g., round(total, 2))


# 📝 Variables

## Key Ideas
- Variables store values (strings, numbers, etc.) so we can reuse them later.
- They act like *labels* attached to values in memory.
- `#` is used for **comments** → these explain code but don’t run.

## Example (basic travel/tax calculation)
```python
name = "Thomas"              # variable = string
tax_rate = 0.14              # variable = number (float)
subtotal = 20                # variable = number (int)
tax = subtotal * tax_rate    # multiply subtotal by tax
total = subtotal + tax       # add tax to subtotal
print(f"Hello, {name}. Your total is {total}.")
