def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    else:
        try:
            if denominator == 0:
                raise ZeroDivisionError
            elif type(numerator)==str or type(denominator)==str:
                raise ValueError
            
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
        
        else:
            return f"The result of the division is {numerator/denominator}"
