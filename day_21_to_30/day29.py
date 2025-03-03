"""Day 29: Middle Figure 
 
Write a function called middle_figure that 
takes two parameters  a, and  b.  
The  two  parameters  are  strings.  
The  function  joins  the  two strings and 
finds the  middle element.  
If  the combined string  has a middle  element,  
the  function  should  return  the  element,  
otherwise, return ‘no middle figure’. 
Use ‘ make love’ as an argument for a and ‘not wars’ as an argument for b. 
Your function should return ‘e’ as the middle element. 
Whitespaces should be removed."""

def middle_figure(a, b):
    new_a = a.replace(" ", "").strip()
    new_b = b.replace(" ", "").strip()

    joined_str = new_a + new_b

    if len(joined_str) % 2 != 0:    # 15 -> True
        half = int(len(joined_str)/2)   # 15/2 = 7
        return f"middle element: {joined_str[half]}"
    else:
        return "no middle elemet"


        
print(middle_figure(' make love','not wars'))
print(middle_figure(' make love','not war'))