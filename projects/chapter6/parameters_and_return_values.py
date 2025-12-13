# celsius_to_fahrenheit
def celsius_to_fahrenheit():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"That temperature in Fahrenheit is: {fahrenheit}")
    return fahrenheit


# is_even
def is_even():
    even_num = input("Enter a number: ")
    number = int(even_num)

    if number % 2 == 0:
        print(f"{number} is even.")
        return True
    else:
        print(f"{number} is not even.")
        return False


# repeat_text
def repeat_text():
    text = input("Enter a string to repeat: ")
    repeat = 4   # or: int(input("How many times? "))
    result = text * repeat
    print(result)
    return result


# --- CALL THE FUNCTIONS --- 
celsius_to_fahrenheit()
is_even()
repeat_text()

 