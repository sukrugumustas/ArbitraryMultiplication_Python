#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author                : Şükrü Gümüştaş
# e-mail                : sukrugumustas@gmail.com
# web                   : http://www.sukrugumustas.com.tr
# For other projects    : https://www.github.com/sukrugumustas
import re


def main():
    while True:
        firstnumber = input('Please enter the first number: ')
        if re.match('^[+-]?\\d+$', firstnumber):  # break if input matches only digits and/or +, - at the beginning
            break
        print('[Invalid Characters (Must be 0-9, +, -)]: ' + firstnumber)  # otherwise warn the user
    while True:
        secondnumber = input('Please enter the second number: ')
        if re.match('^[+-]?\\d+$', secondnumber):  # break if input matches only digits and/or +, - at the beginning
            break
        print('[Invalid Characters (Must be 0-9, +, -)]: ' + secondnumber)  # otherwise warn the user
    # if both numbers are 0, it is undefined
    if re.match('^[+-]?[0]+$', firstnumber) and re.match('^[+-]?[0]+$', secondnumber):
        print('0 times 0 is undefined!')
    # if one of the inputs is 0, the result will be zero so we check each element of inputs if they are 0
    # if they are, we simply print 0.
    elif re.match('^[+-]?[0]+$', firstnumber) or re.match('^[+-]?[0]+$', secondnumber):
        print('The result is 0.')
    # otherwise we calculate
    else:
        # if one of the inputs has negative value, result will be negative, otherwise it will always be positive
        isnegative = (firstnumber[0] == '-') ^ (secondnumber[0] == '-')
        # deleting the +, - signs and 0s at the beginning if there is and converting the input to the list of integers
        firstnumber = [int(x) for x in re.sub('^[+-0]+', '', firstnumber)]
        secondnumber = [int(x) for x in re.sub('^[+-0]+', '', secondnumber)]
        # will be used to hold where we left at the result while calculating
        index = len(firstnumber) + len(secondnumber) - 1
        # creating a list of 0s as in the length of possible multiply
        result = (index + 1) * [0]
        # we need to use the reversed lists of multiplicants
        for i in reversed(firstnumber):
            carryout = 0
            # will be used to continue from the leftmost number
            # calculation will start from the rightmost number and go to the leftmost
            index_2 = index
            for j in reversed(secondnumber):
                mul = carryout + i * j + result[index_2]
                result[index_2] = int(mul % 10)
                carryout = int(mul / 10)
                index_2 -= 1
            # if there is carryout from the last two numbers we should add it to the left most number as well
            result[index_2] += carryout
            index -= 1
        # if the result is negative we print - sign before printing the result
        # if the result has leading 0s at the beginning we strip them from the string
        print('The result is ' + ('-' if isnegative else '') + str(''.join(map(str, result))).lstrip('0') + '.')
    return


if __name__ == '__main__':
    main()
