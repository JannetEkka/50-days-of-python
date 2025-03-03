"""Day 36: Count String 
 
Write a function called count that takes one argument a string, and 
returns a dictionary of how many times each element appears in the string. 
For example ‘hello’ should return:  {‘h’:1,’e’: 1,’l’:2, ‘o’:1}."""

def count(str):
    dict_str = {}
    for ele in str:
        if ele in dict_str:
            dict_str[ele] += 1
        else:
            dict_str[ele] = 1
    return dict_str

print(count('hello'))