"""Day 32: Password Validator 
 
Write a function called password_validator. 
The function asks the user to enter a password. 
A valid password should have at least one upper letter, one lower letter, and  one number. 
It should not be less than 8 characters long. 
When the user enters a password, 
the function  should  check  if  the  password  is  valid.  
If  the  password  is valid, 
the function should return the valid password. 
If the password is  not  valid,  
the  function  should  tell  the  users  the  errors  in  the password  and  
prompt  the  user  to  enter  another  password.  
The code should only stop once the user enters a valid password. 
(use while loop)"""

def password_validator():
    while True:
        password = str(input("Enter password: "))
        errors = []
        
        if len(password) < 8:
            errors.append("Entered password cannot be less than 8 characters")
        if not any(char.isupper() for char in password):
            errors.append("Entered password needs to have at least 1 uppercase letter")
        if not any(char.islower() for char in password):
            errors.append("Entered password needs to have at least 1 lowercase letter")
        if not any(char.isnumeric() for char in password):
            errors.append("Entered password needs to have at least 1 number")
        if errors:
            for e in errors:
                print(e)
            continue
        else:
            print("Password entered is valid!")
            return password

password_validator()