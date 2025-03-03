"""Day 39: Password Generator 
 
Create  a  function  called  generate_password  
that  generates  any length  of  password  for  the  user.  
The  password  should  have  a random  mix  of  upper  letters,  lower  letters,  numbers,  and punctuation  symbols.  
The  function  should  ask  the  user  how strong they want the password to be. 
The user should pick from  - weak, strong, and very strong. 
If the user picks weak, the function should  generate  a    5  character  long  password.  
If  the  user  picks strong,  generate  an  8  character  password  
and  if  they  pick  very strong, generate a 12 character password."""

import random
import string

def generate_password():
    strength = input("How strong do you want the password to be? (weak, strong, and very strong): ")
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    length = 0
    password = ''

    if strength == 'weak':
        length = 5
    elif strength == 'strong':
        length = 8
    elif strength == 'very strong':
        length = 12
        
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

print(generate_password())