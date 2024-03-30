class RomanNumeralCalc:
    def __init__(self):
        pass

    def input_is_valid(self, roman_string):
        valid_nums = ["M", "D", "C", "L", "X", "V", "I"]
        for i in range(len(roman_string)):
            if roman_string[i] not in valid_nums:
                return False
        return True

    def roman_to_decimal(self, roman):
        # Dictionary containing roman numeral values
        ROMAN_VALUES = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

        # total_value variable tracks the decimal value for the roman numeral expression
        i = 0
        total_value = 0
        while i < len(roman):
            # Check if subtractive notation rule needs to be used
            if (i + 1 < len(roman)) and (ROMAN_VALUES[roman[i]] < ROMAN_VALUES[roman[i + 1]]):
                total_value += ROMAN_VALUES[roman[i + 1]] - ROMAN_VALUES[roman[i]]
                i += 2

            # Subtractive notation not present, just add as normal
            else:
                total_value += ROMAN_VALUES[roman[i]]
                i += 1
        return total_value

    def decimal_to_roman(self, decimal):
        ROMAN_LETTERS = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X",
                         9: "IX",
                         5: "V", 4: "IV", 1: "I"}
        ROMAN_DECIMAL = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        roman_string = ""
        # You can basically use this "greedy" algorithm to find the
        for number in ROMAN_DECIMAL:
            num_letters = decimal // number
            roman_string += num_letters * ROMAN_LETTERS[number]
            decimal = decimal % number
        return roman_string
