"""Day 20: Capitalize First Letter
Write a function called capitalize. 
This function takes a string as an argument and 
capitalizes the first letter of each word. 
For example, ‘i like learning’ becomes ‘I Like Learning’."""

def capitalize(sentence):
    words = sentence.split(' ')  # Split the sentence into words
    capitalized_words = []
    
    for word in words:   # get the first characters of each word
        # Capitalize the first letter of each word and add the rest of the word
        if word:
            capitalized_word = word[0].upper() + word[1:]
        else:
            ''
        capitalized_words.append(capitalized_word)
    return ' '.join(capitalized_words)  # Join the list back into a single string

print(capitalize('i like learning'))

def capitalize2(sentence):
    return ' '.join(word[0].upper() + word[1:] for word in sentence.split(' '))

print(capitalize2('i like learning'))