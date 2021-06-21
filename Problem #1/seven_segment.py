from os import system, name
from time import sleep

# Template of seven segment for each number
# Each number represents as 3 x 4 array
segment_str = '''
 __      __  __     
|  |   | __| __||__|
|__|   ||__  __|   |
 __  __  __  __  __ 
|__ |__    ||__||__|
 __||__|   ||__| __|
    
    
 __ 
'''

# Seperator
seperator = ' · '

# Ignore first newline character and split to each line
segment_str = segment_str[1:].split('\n')

# The method for generating segment for each number
def generateSegment(num, isInvalid = False):
    if isInvalid:
        return [(6, 0), (6, 0)]

    extractList = []
    while len(extractList) != 2:
        digit = num % 10
        row = 0
        if digit >= 5:
            row = 3
            digit -= 5
        extractList.append((row, digit * 4))
        num //= 10
    return extractList[::-1]

# The method for printing the seven segment
def printSevenSegment(hours, minutes, seconds):
    invalidTime = False
    if minutes > 59 or seconds > 59:
        invalidTime = True

    hours = generateSegment(hours, invalidTime)
    minutes = generateSegment(minutes, invalidTime)
    seconds = generateSegment(seconds, invalidTime)
    allSegment = hours + minutes + seconds
    for i in range(3):
        for idx, (row, column) in enumerate(allSegment):
            for columnPrint in range(column, column + 4):
                print(segment_str[row + i][columnPrint], end='')
            if idx % 2 != 0 and idx != 5 and i != 0:
                print(seperator, end='')
            elif idx % 2 != 0 and i == 0:
                print('   ', end='')
            else: 
                print(' ', end='')
        print()
hours, minutes, seconds = map(int, input().split(':'))
