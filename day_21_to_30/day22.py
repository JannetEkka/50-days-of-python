"""Day 22: Add Under_Score
Create three functions. 
The first called add_hash takes a string and 
adds  a  hash  #  between  the  words.  
The  second  function  called add_underscore  
removes  the  hash(#)  and  replaces  it  with  an underscore  (  _  )  
The  third  function  called  remove_underscore, 
removes  the  underscore  and  replaces  it  with  nothing.  
if  you  pass ‘Python’ as an argument for the three functions, and 
you call them at the same time like: 
print(remove_underscore(add_underscore(add_hash('Python'))))  
it  should return ‘Python’."""

def add_hash(str):
    hash = str.replace(" ",'#')
    print("add_hash function  result: ",hash)
    return hash

def add_underscore(str):
    underscore = str.replace('#','_')
    print("add_underscore function result: ", underscore)
    return underscore

def remove_underscore(str):
    remove = str.replace('_','')
    print("remove_underscore function result: ", remove)
    return remove

print(remove_underscore(add_underscore(add_hash('python is great'))))
print(remove_underscore(add_underscore(add_hash('Python'))))
