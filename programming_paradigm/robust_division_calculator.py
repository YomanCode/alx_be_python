def safe_divide(numerator, denominator):
    try:
        num1 = float(numerator)
        num2 = float(denominator)
        
        result = num1 / num2
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Please enter numeric values only."