"""Day 25: All the Same 
 
Create a function called  all_the_same that 
takes one argument, a string, a list, or a tuple and 
checks if all the elements are the same. 
If the elements are the same, the function should return True. 
If not, it should return False. 
For example, [‘Mary’, ‘Mary’, ‘Mary’] should return True."""

def all_the_same(data):
    if len(data) == 0:
        return True
    
    first_ele = data[0]
    for item in data:
        if item != first_ele:
            return False
    
    return True

# Test with a list
print(all_the_same(['Mary', 'Mary', 'Mary']))
print(all_the_same([1, 2, 1]))
print(all_the_same([7, 7, 7, 7, 7]))

# Test with a tuple
print(all_the_same((5, 5, 5, 5)))
print(all_the_same((5, 10, 5)))
print(all_the_same(()))

# Test with a string
print(all_the_same("aaaa"))
print(all_the_same("abc"))
print(all_the_same(""))

