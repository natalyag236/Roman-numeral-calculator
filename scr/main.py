import re
import sys

# Convert a Roman numeral string into an integer
def roman__int(roman):
    """
    Converts the Roman numeral string to a integer

    Args:
        roman : represents the string for roman numeral 
    Returns:
        the integer relates to roman numeral 
    """
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0

    for numeral in roman:
        current_value = roman_numerals[numeral]

        if current_value > prev_value:
            total += current_value - 2 * prev_value
        else:
            total += current_value

      
        prev_value = current_value

    return total

# Convert an integer to a Roman numeral string
def int_roman(num):
    """
    Conversts the interger to a Roman Numeral

    Args:
        num  : converts the integers to a roman numeral

    Returns:
        the roman numeral that relates to the integer and if the 
        roman numeral is greater than 3999 than it will print a message.

    """
    conversion= {
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
    
    # Loop through the values in the conversio
    for value in conversion:
        # while the number is greater than or equal to current value 
        while num >= value:
            roman_numeral += conversion[value]
            num -= value

    return roman_numeral

# Process and evaluate an algebraic expression that includes Roman numerals
def equation(expression):
    """
    the function coverts the roman numeral operation into a integer then coverts 
     the results back to roman numeral 
    Args:
        expression is the algebraic expression that invloves the roman numerals
    Returns:
        the answers to the algebraic expression as roman numeral
    """
    try:
        # Helper function to replace Roman numerals with their integer equivalents
        def convert_roman(match):
            roman_numeral = match.group(0)  # Get the matched Roman numeral
            return str(roman__int(roman_numeral))  # Convert it to integer as a string

        # Searchs for the roman numeral and coverts it into a interger
        expression_with_integers = re.sub(r'[IVXLCDM]+', convert_roman, expression)

        result = eval(expression_with_integers)

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
        # Catch any unexpected errors and return a readable message
        return "The expression is invalid. Please try again."

# User will enter input only in the command-line 
def main():
  """
  The main function handles the command line input
  Args:
    user_input is expects the user to put an algebraic experssion in the command line

  Returns:
    will display the answers in roman numeral 
  """
if len(sys.argv) < 2:
    sys.exit(1)
    
    user_input = sys.argv[1]
    
    # Evaluate the expression and display the result
    final_result = equation(user_input)
    print(final_result)

if __name__ == "__main__":
    main()
