"""Day 21: List of Tuples
Write a function called make_tuples 
that takes two lists,
equal lists,
and combines them into a list of tuples. 
For example if list a is [1,2,3,4] and list b is [5,6,7,8], 
your function should return [(1,5),(2,6),(3,7),(4,8)]."""

def make_tuples(a, b):
    if len(a) != len(b):
        return "Lists must be of equal length!"
    tup =[]
    for n in range(len(a)):
        tup.append((a[n],b[n]))
    return tup
    
print(make_tuples([1,2,3,4],[5,6,7,8]))