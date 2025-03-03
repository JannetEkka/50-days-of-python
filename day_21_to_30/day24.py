"""Day 24: Average Calories 
 
Create a function called average_calories 
that calculates the average calories intake of a user. 
The function should ask the user to input their calories intake  
for any number of days and
once they hit ‘done’ it should calculate and return the average intake."""

def average_calories():
    total_calories = 0
    days = 0

    while True:
        calories = input("Enter calories (kcal) for each day. Enter 'done' when done.\n")
        
        if calories .lower() == 'done':
            break

        try:
            calories = float(calories)
            total_calories += calories
            days += 1
        except Exception:
            print("Values invalid. Please enter a number or 'done'")

    if days == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    
    avg = total_calories/days
    return f"Your average intake for {days} days is: {avg:.2f} kcal per day"
    
print(average_calories())