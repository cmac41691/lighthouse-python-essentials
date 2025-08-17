# Intro to Data & Logic

## Key ideas (in my words)
- Data must be structured so a computer can use it.
- Logic = the rules/steps we apply to that data.

## Example structures (mental model)
- JSON:
```json
{"pizza":{"size":"large","toppings":["pepperoni","mushrooms"],"price":14.99}}

-XML
<pizza><size>large</size><toppings><topping>pepperoni</topping><topping>mushrooms</topping></toppings><price>14.99</price></pizza>

- Python Equivalent
pizza = {"size":"large","toppings":["pepperoni","mushrooms"],"price":14.99}
1. Choose the structure(dict/list)
2. Store values(strings, number, list)
3. Access values and print/ compute

## Tricky parts to revist
- Choosing between list vs dict
- Remembering nested access (e.g., pizza["topping"][0])
