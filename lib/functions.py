#!/usr/bin/env python3
def greet_programmer():
    print("Hello, programmer!")

greet_programmer()

    

def greet(name):
    print(f"Hello, {name}!")
    

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

    

def add(num1, num2):
    result =num1 + num2
    return result
sum_result = add(45,55)
print(sum_result)

def halve(number):
    result = number / 2
    return result


integer_input = 10
halved_integer = halve(integer_input)
print(halved_integer)

# Call the function with a float input
float_input = 7.5
halved_float = halve(float_input)
print(halved_float)

