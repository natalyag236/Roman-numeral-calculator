import re
import sys

def roman_int(roman):
    """
    Converts the Roman numeral string to an integer

    Args:
        roman : represents the string for a Roman numeral 
    Returns:
        the integer related to the Roman numeral 
    """
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0

    for numeral in roman:
        current_value = roman_numerals.get(numeral)

        if current_value is None:
            raise ValueError(f"Invalid Roman numeral: {numeral}")

        if current_value > prev_value:
            total += current_value - 2 * prev_value
        else:
            total += current_value

        prev_value = current_value

    return total

def int_roman(num):
    """
    Converts the integer to a Roman Numeral

    Args:
        num : converts the integer to a Roman numeral

    Returns:
        the Roman numeral related to the integer. If the 
        integer is greater than 3999, a message is returned.
    """
    conversion = {
        1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC",
        50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
    }

    if num > 3999:
        return "You’re going to need a bigger calculator."
    elif num == 0:
        return "Roman numerals don’t have a zero."
    elif num < 0:
        return "Negative numbers can’t be written in Roman numerals."

    roman_numeral = ""
    
    # Loop through the values in the map, appending Roman numerals while reducing the number
    for value in conversion:
        while num >= value:
            roman_numeral += conversion[value]
            num -= value

    return roman_numeral

def equation(expression):
    """
    Converts the Roman numeral operation into an integer then converts 
    the result back to a Roman numeral 

    This function:
    - Converts any Roman numerals in the expression into integers.
    - Evaluates the mathematical expression while respecting parentheses and order of operations.
    - Converts the resulting integer back to a Roman numeral.
    Args:
        expression: the algebraic expression involving Roman numerals
        
    Returns:
        the result of the algebraic expression as a Roman numeral,or an error message if the expression is invalid.
    """
    try:
        # Replace Roman numerals with their integer equivalents
        def convert_roman(match):
            roman_numeral = match.group(0)  # Get the matched Roman numeral
            return str(roman_int(roman_numeral))  # Convert it to integer as a string

        def grouped_expr(expr):
            while '(' in expr:
                expr = re.sub(r'\(([^()]+)\)', lambda m: str(grouped_expr(m.group(1))), expr)
            return eval(re.sub(r'[IVXLCDM]+', convert_roman, expr))

        # Evaluate the expression respecting parentheses and Roman numeral conversions
        result = grouped_expr(expression)

        # Handle special cases for Roman numeral results
        if isinstance(result, float):
            return "Roman numerals don’t support fractions."
        if result == 0:
            return "Roman numerals don’t include zero."
        if result < 0:
            return "Negative numbers can’t be written in Roman numerals."
        if result > 3999:
            return "You’re going to need a bigger calculator."

        # Convert the result back into a Roman numeral and return it
        return int_roman(int(result))

    except Exception as error:
        return "The expression is invalid. Please try again."

def main():
    """
    The main function handles the command line input
    
    This function:
    - Accepts input from the command line, either as a single Roman numeral or an algebraic expression.
    - If the input is a single Roman numeral, it converts it to an integer and displays the result.
    - If the input is an algebraic expression with Roman numerals, it evaluates the expression
      and displays the result in Roman numerals.

    Args:
        user_input: expects the user to input an algebraic expression in the command line
    Returns:
        Displays the answer in Roman numerals 
        Also displays the English conversion for a single Roman numeral (e.g., III = 3)
    """
    if len(sys.argv) < 2:
        return
    
    user_input = ' '.join(sys.argv[1:])

    # If the input is a single Roman numeral, convert it to an integer
    if re.match(r'^[IVXLCDM]+$', user_input):
        value = roman_int(user_input)
        print(f"English conversion: {value}")
    else:
        final_result = equation(user_input)
        print(final_result)

if __name__ == "__main__":
    main()
 
