"""Extra Challenge: Set or list 
You want to implement a code that will search for a number in a range. 
You have a decision to make as to whether to store the number in a set or a list. 
Your decision will be based on time. 
You have to pick a data type that executes faster. 
You have a range and you can either store it in a set or a list 
depending on which one executes faster when you are searching for a number in the range. 
See below: 
a = range(10000000) 
x = set(a) 
y = list(a) 
Let’s say you are looking for a number 9999999 in the range above. 
Search for this number in the list and the set. 
Your challenge is to find which code executes faster. 
You will pick the one that executes quicker, lists, or sets.
 Run the two searches and time them."""

import timeit

setup = '''a = list(range(10000000))

def list_search(num):
    x = set(a)
    if num in x:
        return True
    
def set_search(num):
    y = list(a)
    if num in y:
        return True'''
    
list_time = timeit.timeit('list_search(9999999)', setup = setup, number=10)
print(f'List time: {list_time}')
set_time = timeit.timeit('set_search(9999999)', setup = setup, number=10)
print(f'Set time: {set_time}')

if list_time > set_time: 
    print('Best time was taken by Set')
else:
    print('Best time was taken by List')