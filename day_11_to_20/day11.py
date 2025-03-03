"""Day 11: Are They Equal?
Write a function called equal_strings. The function takes two strings
as arguments and compares them. If the strings are equal (if they
have the same characters and have equal length), it should return
True, if they are not, it should return False. For example, ‘love’ and
‘evol’ should return True."""

def equal_strings(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False
    
print(equal_strings('lovel', 'evol'))  # False (different lengths)
print(equal_strings('love', 'evol'))   # True (same characters)
print(equal_strings('love', 'hate'))   # False (different characters)
