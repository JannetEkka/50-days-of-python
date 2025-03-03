"""Day 28: Return Indexes 
 
Write a function called index_position. 
This function takes a string as  a  parameter  and  
returns  the  positions  or  indexes  of  all  lower letters in the string. 
For example ‘LovE’ should return [1,2]."""

def index_position(str):
    lower_lst = []
    for i in range(len(str)):
        if str[i].islower():
            lower_lst.append(i)
    return lower_lst
        

print(index_position('LovE'))