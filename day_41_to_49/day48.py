"""Day 48: Binary Search 
 
Write a function called search_binary 
that searches for the number 22 in the following list 
and returns its index. 
The function should take two parameters, 
the list and the item that is being searched for. 
Use binary search (iterative Method). 
list1 = [12, 34, 56, 78, 98, 22, 45, 13]"""

def search_binary(lst, target) -> int:
    list_tuples = [(val, idx) for idx, val in enumerate(lst)]
    list_tuples.sort()

    left = 0
    right = len(lst)-1

    while left<=right:
        mid = (left+right)//2
        
        mid_val, og_idx = list_tuples[mid]

        if mid_val == target:
            return og_idx
        elif mid_val < target:
            left = mid+1
        else:
            right = mid+1

    return -1

target = 22
list1 = [12, 34, 56, 78, 98, 22, 45, 13]

print(search_binary(list1, target))
