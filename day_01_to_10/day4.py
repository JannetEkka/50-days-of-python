# Day 4: Only Floats

def only_floats(a, b):
    """
    Write a function called only_floats, 
    which takes two parameters a and b, 
    and returns 2 if both arguments are floats, 
    returns 1 if only one argument is a float, 
    and returns 0 if neither argument is a float. 
    If you pass (12.1, 23) as an argument, your function should return a 1.
    """
    if type(a) == float and type(b) == float:
        return 2
    elif type(a) == float or type(b) == float:
        return 1
    else:
        return 0
    
print(only_floats(12.3,1))
print(only_floats(12.3,12.2))
print(only_floats(12,1))
print(only_floats(12.3,'a'))
print(only_floats('2a','a'))