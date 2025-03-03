"""
Day 13: Pay Your Tax
Write a function called your_vat. 
The function takes no parameter.
The function asks the user to input the price of an item and VAT (vat should be a percentage). 
The function should return the price of the item plus VAT. 
If the price is 220 and, VAT is 15% 
your code should return a vat inclusive price of 253. 
Make sure that your code can handle ValueError. 
Ensure the code runs until valid numbers are entered. 
(hint: Your code should include a while loop).
"""

def your_vat():
    while True:
        try:    
            price = float(input("Price: "))
            vat = float(input("VAT(%): "))

            if price <= 0:
                print("Price must be greater than 0")
                continue
            if vat <0 or vat > 100 :
                print("VAT must be between 0 and 100")
                continue

            price_vat = price+(price*vat/100)

            return f"VAT inclusive Price: {price_vat:.1f}"
        
        except ValueError:
            print("Enter valid price or VAT")
            continue

print(your_vat())