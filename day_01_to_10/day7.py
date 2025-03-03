# Day 7: A String Range

import numpy as np

def string_range(num):
    """
    Write a function called string_range that 
    takes a single number and returns a string of its range. 
    The string characters should be separated by dots(.) 
    For example, if you pass 6 as an argument, your function should return ‘0.1.2.3.4.5’.
    """
    numbers = range(num)
    strings = (str(x) for x in numbers)
    result = '.'.join(strings)

    return result

print(string_range(6))

# Time Complexity: O(n)
# Space Complexity: O(n)