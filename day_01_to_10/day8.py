# Day 8: Odd and Even

def odd_even(numbers):
    """
    Write a function called odd_even that has one parameter
    and takes a list of numbers as an argument. 
    The function returns the difference between the largest even number in the list and 
    the smallest odd number in the list. 
    For example, if you pass [1,2,4,6] as an argument 
    the function should return 6 -1= 5.
    """
    # Any real number will be LARGER than negative infinity
    # So the first even number we find will replace this
    largest_even = float('-inf')
    
    # Any real number will be SMALLER than positive infinity
    # So the first odd number we find will replace this
    smallest_odd = float('inf')

    for num in numbers:
        if num%2==0:
            largest_even = max(largest_even, num)
            
        else:
            smallest_odd = min(smallest_odd, num)

    print("largest even number in list: ", largest_even)
    print("smallest even number in list", smallest_odd)

    diff = largest_even-smallest_odd
    return diff

test_list = [13,3,4,5,10,32]
print("Difference: ",odd_even(test_list))