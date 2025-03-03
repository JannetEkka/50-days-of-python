"""Day 38: Guess a Number 
 
Write a function called guess_a_number. 
The function should ask a user to guess a randomly generated number. 
If the user guesses a higher number, the code should tell them that the guess is too high, 
if the user guesses low, the code should tell them that their guess is too low. 
The user should get a maximum of three guesses. 
When the user  guesses  right,  the  code  should  declare  them  a  winner.  
After three wrong guesses, the code should declare them a loser"""

import random

def guess_a_number():
    attempt = 1
    max_attempts = 3
    sys_int = random.randint(0,9)

    while attempt <= max_attempts:
        users_guess = int(input("Guess a number (0-9): "))
        
        if users_guess > sys_int:
            print("Your guess is too high!")
        elif users_guess < sys_int:
            print("Your guess is too low!")
        else:
            print("Winner!")
            return
        attempt += 1
        
    print(f"Loser! The correct number was {sys_int}.")

print(guess_a_number())

