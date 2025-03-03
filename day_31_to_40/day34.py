"""Day 34: Just Digits 
 
In  this  challenge,  
copy  the  text  below  and  save  it  as  a  CSV  file. 
Save it in the same folder as your Python file. 
Save it as python.csv. 
Write a function called just_digits that reads the text from the CSV 
file and returns only digit elements from the file. Your function should 
return 1991, 2, 200, 3, 2008 as a list of strings. 
 
“Python  was  released  in  1991  for  the  first  time.  Python 2  was released in 2000 and introduced new features, such as list comprehensions and  a cycle-detecting garbage  collection  system (in addition to reference counting). Python 3 was released in 2008 and was a major revision of the language that is not completely backward-compatible.” 
Source: Wikipedia"""

import pandas as pd

def just_digits_pd():
    df = pd.read_csv("python.csv", header=None, sep = '\r\n', names = ['texts'], engine='python')
    text = ''.join(df['texts'].astype(str))
    numbers = [word for word in text.split() if word.isdigit()]
    return numbers

def just_digits():
    with open('python.csv', 'r') as file:
        text = file.read()
    
    numbers = [word for word in text.split() if word.isdigit()]
    return numbers

print(just_digits_pd())
print(just_digits())

