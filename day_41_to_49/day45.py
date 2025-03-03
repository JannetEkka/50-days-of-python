"""Day 45: Words and Special Characters 
 
Write  a  function  called  analyse_string  
that  returns  the  number  of special  characters  (#$%&'()*+,-./:;<=>?@[\]^_`{|}~),  
words,  and, total characters (all letters and special characters minus whitespaces) in a string. 
Return everything in a dictionary format: 
{“special character”:  “number”,  “words”:  “number”,  “total characters”: “number”} 
 Use the string below as an argument: 
 “Python has a string format operator %. This functions analogously to  printf  format  strings  in  C,  e.g.  "spam=%s  eggs=%d"  %  ("blah",  2) evaluates to "spam=blah eggs=2". 
 Source Wikipedia."""

import string

def analyse_string(str: str)->dict:
    str_dict = {
        "special character": 0,
        "words": 0,
        "total characters": 0
    }

    spe_chars = set(string.punctuation)
    count = 0
    for char in str:
        if char in spe_chars:
            count += 1
    spec_char_count = (char for char in str if char in spe_chars)
    str_dict['special character'] = spec_char_count

    all_words = str.split()
    words = len(all_words)
    str_dict["words"] = words
    
    total = ''.join(all_words)
    total_count = len(total)
    str_dict["total characters"] = total_count

    return str_dict

print(analyse_string('Python has a string format operator %. This functions analogously to  printf  format  strings  in  C,  e.g.  "spam=%s  eggs=%d"  %  ("blah",  2) evaluates to "spam=blah eggs=2'))