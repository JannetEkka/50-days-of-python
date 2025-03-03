"""Extra Challenge: Sort by Last Name  
You  work  for  a  local  school  in  your  area.  
The  school  has  a  list  of names of students saved in a list. 
The school has asked you to write a program that takes a list of names and 
sorts them alphabetically. 
The names should be sorted by last names. 
Here is a list of names: 
[‘Beyonce Knowles, ‘Alicia Keys’, ‘Katie Perry’,  ‘Chris Brown’,’ Tom Cruise’] 
Your code should not just sort them alphabetically, but it should also switch the names (the last name must be the first). 
Here is how your code output should look: 
['Brown Chris', 'Cruise Tom', 'Keys Alicia', 'Perry Katie', 'Knowles Beyonce'] 
Write a function called sorted_names."""

def sorted_names(names_list):
    new_switched_names_list = []
    for name in names_list:
        new_name = name.split()
        f_name = new_name[0]
        l_name = new_name[1]
        new_switched_names = l_name + ' ' + f_name
        new_switched_names_list.append(new_switched_names)

    sorted_list = sorted(new_switched_names_list)
    return sorted_list

print(sorted_names(['Beyonce Knowles', 'Alicia Keys', 'Katie Perry', 'Chris Brown', 'Tom Cruise']))