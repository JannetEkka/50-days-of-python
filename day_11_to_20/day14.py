"""Day 14: Flatten the List"""
"""Write a function called flat_list that takes one argument, a nested list. 
The function converts the nested list into a one-dimension list.
For example [[2,4,5,6]] should return [2,4,5,6]."""

def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

def flat_list(nested_list):
    result = []
    for item in flatten(nested_list):
        result.append(item)
    return result

print(flat_list([[2,4,5,6]]))
print(flat_list([[1,2], [2,4,5,6]]))
print(flat_list([['a','b'], [2,4,5,6]]))