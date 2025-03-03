# Day 3: Register Check

def register_check(dict):
    """
    Write a function called register_check
    that checks how many students are in school.
    The function takes a dictionary as parameter.
    If the student is in school, the dictionary says 'yes'.
    If the student is not in school, the dictionary says 'no'.
    Your function should return the number of students in school.
    """
    count = 0
    for item in dict.values():
        if item == 'yes':
            count += 1
    return count
    
register = {'Michael':'yes', 'John':'no', 'Peter':'yes', 'Mary':'yes'}
print(register_check(register))