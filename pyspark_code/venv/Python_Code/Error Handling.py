# Error Handling in Python
# Python provides a mechanism to handle runtime errors via exception handling using try, except, else, and finally blocks.

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter valid numbers.")
else:
    print(f"The result of {num1} / {num2} is {result}")
finally:
    print("Execution finished.")

	

# Raising Custom Exceptions
# You can define custom exceptions by inheriting from Python's built-in Exception class.

class NegativeNumberError(Exception):
    pass

def check_positive_number(num):
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    return num

try:
    number = int(input("Enter a positive number: "))
    check_positive_number(number)
except NegativeNumberError as e:
    print(e)







