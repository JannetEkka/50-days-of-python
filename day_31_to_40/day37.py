"""Day 37: Count the Vowels 
 
Create a function called count_the_vowels. 
The function takes one argument, a string, 
and returns the number of vowels in the string. 
For example ‘hello’ should return 2 vowels. 
If a vowel appears in a string more than once it should be  counted as one. 
For example, ‘saas’ should return 1 vowel. 
Your code should count lowercase and uppercase vowels."""

def count_the_vowels(str):
    vowels = set()
    vowels_set = "'a','e','i','o','u','A','E','I','O','U'"
    for char in str:
        if char in vowels_set:
            vowels.add(char)
    
    return len(vowels)
        
print(count_the_vowels('saas'))
print(count_the_vowels('SAAS'))
print(count_the_vowels('aejvsjdnioJXNNJINSND'))