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

# Input
hours, minutes, seconds = map(int, input().split(':'))
