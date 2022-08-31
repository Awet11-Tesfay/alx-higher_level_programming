#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str):
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        rs = roman_string
        num = 0
        for l in range(len(rs)):
            if l > 0 and (rom[rs[l]] > rom[rs[l - 1]]):
                num += rom[rs[l]] - (2 * rom[roman_string[l - 1]])
            else:
                num += rom[rs[l]]
        return num
    return (0)
