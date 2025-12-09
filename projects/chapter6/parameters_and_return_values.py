def add_number():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    result = num1 + num2
    print(f"The total is {result}")
    return result


def calculate_area():
    base = int(input("Enter the base: "))
    height = int(input("Enter the height: "))

    area = (base * height) / 2
    print(f"The area is {area}")
    return area


# call the functions to test them
add_number()
calculate_area()
 