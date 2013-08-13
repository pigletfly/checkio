#!/usr/bin/python
# -*- coding: utf-8 -*-
FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"

def checkio(number):
    if number < 10:
        return FIRST_TEN[number]
    elif number >= 10 and number < 20:
        return SECOND_TEN[number - 10]
    elif number >= 20 and number < 100:
        if number % 10 != 0:
            return OTHER_TENS[number / 10 - 2] + " " + checkio(number % 10)
        else:
            return OTHER_TENS[number / 10 - 2]
    else:
        if number % 100 == 0:
            return FIRST_TEN[number / 100] + " " + HUNDRED
        else:
            return FIRST_TEN[number / 100] + " " + HUNDRED + " " + checkio(number % 100)




if __name__ == "__main__":
    print checkio(4)
    print checkio(143)
    print checkio(12)
    print checkio(101)
    print checkio(212)
    print checkio(40)
