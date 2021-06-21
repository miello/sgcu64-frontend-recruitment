from os import system, name
from time import sleep

'''
Template of seven segment for each number
Each number represents as 3 x 4 array

The number 0 - 4 begin in row index 0
The number 5 - 9 begin at row index 3
The invalid case begins at row index 6
'''
segment_str = '''
 __      __  __     
|  |   | __| __||__|
|__|   ||__  __|   |
 __  __  __  __  __ 
|__ |__    ||__||__|
 __||__|   ||__| __|
    
    
 __ 
'''

# Represent the seperator between hours, minutes and seconds
seperator = ' · '

# Ignore first newline character and split to each line
segment_str = segment_str[1:].split('\n')

'''
The method for generating list segment template for each number
Input:
    num: the number which want to generated the segment
    isInvalid: True if the input is invalid otherwise False
Return:
    List of tuple which in form (x, y)
    x: starting row index in template
    y: starting column index in template 
'''
def generateSegment(num, isInvalid = False):
    # invalid case return the "_" case
    if isInvalid:
        return [(6, 0), (6, 0)]

    extractList = []

    # Loop while until length of final list is two
    while len(extractList) != 2:
        digit = num % 10
        row = 0
        if digit >= 5:
            row = 3
            digit -= 5
        extractList.append((row, digit * 4))
        num //= 10

    # Reverse the final list
    return extractList[::-1]

''' 
The method for printing the seven segment
Input:
    hours: the value of hours
    minutes: the value of minutes
    seconds: the value of seconds
Return:
    None
'''
def printSevenSegment(hours, minutes, seconds):
    # Check the invalid case
    invalidTime = False
    if minutes > 59 or seconds > 59:
        invalidTime = True

    # Generate the template list 
    hours = generateSegment(hours, invalidTime)
    minutes = generateSegment(minutes, invalidTime)
    seconds = generateSegment(seconds, invalidTime)

    # Concatenate all list of segment in order hours -> minutes -> seconds
    allSegment = hours + minutes + seconds

    # Iterate over each row which is three
    for i in range(3):
        # Iterate over each element in allSegment with tracing index
        for idx, (row, column) in enumerate(allSegment):
            # Iterate over each character in template but why plus four ?
            # Because each seven segment have a width four and height three
            for columnPrint in range(column, column + 4):
                print(segment_str[row + i][columnPrint], end='')

            # print seperator if item is the odd element in allSegment and not the first and last element 
            if idx % 2 != 0 and idx != 5 and i != 0:
                print(seperator, end='')

            # print just a space width three when item is the odd element and is in the first row
            elif idx % 2 != 0 and i == 0:
                print('   ', end='')

            # print space width one 
            else: 
                print(' ', end='')

        # print new line
        print()


# Input time
hours, minutes, seconds = map(int, input().split(':'))
