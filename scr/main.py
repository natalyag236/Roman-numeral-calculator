import re
import sys

# Convert a Roman numeral string into an integer
def roman_to_integer(roman_numeral):
    roman_numerals_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    previous_value = 0

    # Iterate through each character in the Roman numeral
    for numeral in roman_numeral:
        current_value = roman_numerals_map[numeral]

        # If the current value is greater than the previous one, adjust accordingly (subtractive notation)
        if current_value > previous_value:
            total += current_value - 2 * previous_value
        else:
            total += current_value

        # Update previous_value for the next loop iteration
        previous_value = current_value

    return total

# Convert an integer to a Roman numeral string
def integer_to_roman(num):
    roman_conversion_map = {
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
    for value in roman_conversion_map:
        while num >= value:
            roman_numeral += roman_conversion_map[value]
            num -= value

    return roman_numeral

# Process and evaluate an arithmetic expression that includes Roman numerals
def evaluate_expression(expression):
    try:
        # Helper function to replace Roman numerals with their integer equivalents
        def convert_roman(match):
            roman_numeral = match.group(0)  # Get the matched Roman numeral
            return str(roman_to_integer(roman_numeral))  # Convert it to integer as a string

        # Use regular expressions to replace Roman numerals with their integer counterparts
        expression_with_integers = re.sub(r'[IVXLCDM]+', convert_roman, expression)

        # Evaluate the modified expression with Python's built-in eval function
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

        # Convert the final result back into a Roman numeral and return it
        return integer_to_roman(int(result))

    except Exception as error:
        # Catch any unexpected errors and return a readable message
        return "The expression is invalid. Please try again."

# Main function that handles only command-line input
def main():
    # Check if the user provided a command-line argument
    if len(sys.argv) < 2:
       
        sys.exit(1)
    
    # Take the expression from the command-line argument
    user_input = sys.argv[1]
    
    # Evaluate the expression and display the result
    final_result = evaluate_expression(user_input)
    print(final_result)

if __name__ == "__main__":
    main()
