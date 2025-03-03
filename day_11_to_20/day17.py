"""Day 17: User Name Generator
Write a function called user_name, that creates a username for the user. 
The function should ask a user to input their name.
The function should then reverse the name and 
attach a randomly issued number between 0 – 9 at the end of the name. 
The function should return the username."""
import random
import re

def user_name():
    name = input("Enter your name: ")
    rev_name = name[::-1]
    num = str(random.randint(0,10))
    return (rev_name+num)

print(user_name())