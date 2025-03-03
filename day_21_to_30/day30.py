"""Day 30: Most Repeated Name 
 
Write a function called repeated_name that 
finds the most repeated name in the following list. 
name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]"""

def repeated_name_dict(names_list):
    dup_dict = {}
    for i in names_list:
        if i in dup_dict:
            dup_dict[i]+=1
        else:
            dup_dict[i]=1

    return max(dup_dict, key=dup_dict.keys())

print(repeated_name_dict(["John", "Peter", "John", "Peter", "Jones", "Peter"]))