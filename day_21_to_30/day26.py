"""Day 26: Sort Words 
 
Write a function called sort_words that 
takes a string of words as an argument,  
removes  the  whitespaces,  and  
returns  a  list  of  letters sorted in alphabetical order. 
Letters will be separated by commas. 
All letters should appear once in the list. 
This means that you sort and remove duplicates. 
For example ‘love  life’ should return as 
['e,f,i,l,o,v']."""

def sort_words(str):
    str_ws = str.replace(" ", "")
    sorted_str = sorted(str_ws)
    res_list = []
    for ele in sorted_str:
        if ele not in res_list:
            res_list.append(ele)

    return res_list

print(sort_words('love  life'))