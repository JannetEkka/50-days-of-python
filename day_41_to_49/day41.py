"""Day 41: Only Words with Vowels 
 
Create a function called words_with_vowels, 
this function takes a string of words 
and returns a list of only words that have vowels in them. 
For example ‘  You  have  no  rhythm’ should return [‘You’,’have’, ‘no’]."""

def words_with_vowels(str):
    vowels_set = {'a','e','i','o','u'}
    words_vowels_list = []
    words = str.split()

    for word in words:
        for ele in word:
            if ele in vowels_set:
                if word not in words_vowels_list:
                    words_vowels_list.append(word)
            
    return words_vowels_list

def words_with_vowels_any(str):
    vowels_set = {'a','e','i','o','u'}
    words_vowels_list = []
    words = str.split()

    for word in words:
        if any(ele in vowels_set for ele in word):
            if word not in words_vowels_list:
                words_vowels_list.append(word)
            
    return words_vowels_list

def words_with_vowels_lc(str):
    vowels_set = set('aeiouAEIOU')
            
    return [word for word in str.split() if any(ele in vowels_set for ele in word)]

print(words_with_vowels('  You  have  no  rhythm'))
print(words_with_vowels_lc('  You  have  no  rhythm'))
