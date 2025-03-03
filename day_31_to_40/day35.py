"""Day 35: Pangram 
 
Write  a  function  called  check_pangram  that  takes  a  string 
and checks if it is a pangram. 
A pangram is a sentence that contains all the letters of the alphabet. 
If it is a pangram, the function should return True, 
otherwise, return False. 
The following sentence is a pangram so it should return True: 
 
'the quick brown fox jumps over a lazy dog'"""

def check_pangram(str):
    letters = set()
    for char in str:
        if char.isalpha():
            letters.add(char.lower())
    if len(letters) == 26:
        return True

def check_pangram_comp(str):
    alphabets = set(char.lower() for char in str if char.isalpha())
    return len(alphabets) == 26

test_str = 'the quick brown fox jumps over a lazy dog'
print(check_pangram(test_str))
print(check_pangram_comp(test_str))