"""Day 40: Pig Latin 
 
Write a function called translate 
that takes the following words and translates them into pig Latin. 
a = 'i love python' 
 
Here are the rules: 
1.  If a word starts with a vowel (a,e, i, o, u) add ‘yay’ at the end. 
For example ‘eat’ will become ‘eatyay’
2.  If a word starts with anything other than a vowel, move the first letter to the end and add ‘ay’ to the end. 
For example ‘day’ will become ‘ayday’. 
Your code should return: iyay ovelay ythonpay"""

def translate(str):
    words = str.split()
    vowels = {'a','e','i','o','u'}  # Set of vowels
    new_words = []

    for word in words:
        if word[0].lower() in vowels:
            new_word = word + 'yay'
        else:
            new_word = word[1:] + word[0] + 'ay'

        new_words.append(new_word)

    new_string = ' '.join(new_words)
    return new_string

a = 'i love python'
print(translate(a))