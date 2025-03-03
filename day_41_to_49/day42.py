"""Day 42: Spelling Checker 
 
Write a function called spelling_checker. 
This code asks the user to  input  a  word  and  
if  a  user  inputs  a  wrong  spelling  it  should suggest the correct spelling 
by asking the user if they meant to type that  word.  
If  the  user  says  no,  it  should ask  the  user  to  enter  the word again. 
If the user says yes, it should return the correct word. 
If  the  word  entered  by  the  user  is  correctly  spelled  
the  function should return the correct word. 
Use the module textblob."""

from textblob import Word

def spelling_checker():
    while True:
        user_word = input("Enter a word: ").lower()
        word = Word(user_word)

        if user_word == word.correct():
            return user_word
        
        suggested_word = word.correct()
        user_choice = input(f"Did you mean '{suggested_word}'? Yes/No: ").lower()

        if user_choice == 'yes':
            return suggested_word
        elif user_choice == 'no':
            print("Try again with a difference word: ")
            continue
        else:
            print("please answer with yes/no.")
            continue
    
print(spelling_checker())