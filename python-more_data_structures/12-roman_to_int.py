#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is not None and type(roman_string) == str:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                'D': 500, 'M': 1000}
        total = 0
        prev = 1001

        for x in roman_string:
            if roman[x] > prev:
                total += roman[x] - (prev * 2)
            else:
                total += roman[x]
            prev = roman[x]
        return total
    return 0
