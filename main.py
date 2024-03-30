from RomanNumeralCalc import RomanNumeralCalc

if __name__ == "__main__":
    roman_calc = RomanNumeralCalc()

    user_input = ""
    while user_input != "quit":
        user_input = input("Please input either a roman numeral expression or a decimal number (type \"quit\" to "
                           "quit): ")
        if roman_calc.input_is_valid(user_input):
            print("Converting " + user_input + " to decimal: ")
            print(roman_calc.roman_to_decimal(user_input))
        elif user_input.isdigit():
            print("Converting " + user_input + " to roman numerals: ")
            print(roman_calc.decimal_to_roman(int(user_input)))
        elif user_input == "quit":
            pass
        else:
            print("Invalid input")
