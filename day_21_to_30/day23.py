"""Day 23: Simple Calculator
Create a simple calculator. 
The calculator should be able to perform basic math operations, add, subtract, divide and multiply.  
The calculator should take input from users.
The calculator should be able to handle ZeroDivisionError, NameError, and ValueError."""

def simple_calculator():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, /, *): ").strip()

        if operator not in ['+', '-', '*', '/']:
            raise ValueError("Invalid operator. Please use +, -, *, or /")
        
        num2 = float(input("Enter second number: "))

        if operator == '+':
            res = num1 + num2
        elif operator == '-':
            res = num1 - num2
        elif operator == '*':
            res = num1 * num2
        else:
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            res = num1 / num2

        return f"{num1} {operator} {num2} = {res}"

    except ValueError as e:
        return f"Please enter valid input. {str(e)}"
    except NameError:
        return "Variable not defined"
    except ZeroDivisionError as e:
        return f"{str(e)}"
    except Exception as e:
        return f"An unexpected error occurred {str(e)}"
    
print(simple_calculator())