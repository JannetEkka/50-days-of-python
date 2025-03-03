def convert_add(str_list):
    """
    Write a function called convert_add that takes a list of strings as an argument
    and converts it into integers
    and sums the list.
    """
    if not str_list:
        return 0
    try:
        int_list = [int(item) for item in str_list]
        return sum(int_list)
    except ValueError:
        print("List must contain numeric strings")

eg_list = ['1','2','3','4','-5',None]
result = convert_add(eg_list)
print(result)