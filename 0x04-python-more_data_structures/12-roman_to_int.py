#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and isinstance(roman_string, str):
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        r_st = roman_string
        numerom = 0
        for l in range(len(r_st)):
            if l > 0 and (rom[r_st[l]] > rom[r_st[l - 1]]):
                numerom += rom[r_s[l]] - (2 * rom[roman_string[l - 1]])
            else:
                numerom += rom[r_st[l]]
        return numerom
    return (0)
