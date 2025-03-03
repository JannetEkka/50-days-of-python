"""Day 16: Sum the List
Write a function called sum_list with one parameter that 
takes a nested list of integers as an argument and 
returns the sum of the integers. For example, if you pass [[2, 4, 5, 6], [2, 3, 5, 6]] as an
argument your function should return a sum of 33."""

def flatten(lst):
    for i in lst:
        if isinstance(i, list):
            yield from flatten(i)
        else:
            yield i

def sum_list(nested_list):
    flat_list = list(flatten(nested_list))
    int_list = [int(i) for i in flat_list]
    return sum(int_list)

print(sum_list([[2, 4, 5, 6], [2, 3, 5, 6]]))