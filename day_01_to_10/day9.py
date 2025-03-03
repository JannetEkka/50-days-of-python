def biggest_odd(numbers):
    """
    Create a function called biggest_odd 
    that takes a string of numbers and 
    returns the biggest odd number in the list.
    For example, if you pass ‘23569’ as an argument, 
    your function should return 9. 
    Use list comprehension.
    """
    odd_numbers = [int(num) for num in str(numbers) if int(num) % 2 != 0]
    return max(odd_numbers)

print(biggest_odd(23456))