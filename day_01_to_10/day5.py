def my_discount():
    """
    Create a function called my_discount.
    The function takes no arguments but asks the user to input the price and the discount(percentage) of the product.
    Once the user inputs the price and discount, it calculates the price after the discount. 
    The function should return the price after the discount.
    For example, if the user enters 150 as price and 15% as the discount, your function should return 127.5.
    """
    # 150 - ((15/100)*150) = 127.5
    p = float(input("Enter price: "))
    d = float(input("Enter discount %: "))
    p_after_d = p - ((d/100)*p)
    
    return p_after_d

print(my_discount())

# Time Complexity: O(1) per attempt
# Space Complexity: O(1)