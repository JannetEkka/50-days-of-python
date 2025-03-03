"""Day 44: Save Emails 
 
Create a function called save_emails. 
This function takes no arguments but asks the user to input email, 
and it saves the emails in a CSV file. 
The user can input as many emails as they want. 
Once they  hit  ‘done’  the  function  saves  the  emails  and  closes  the  file. 
Create  another  function  called  open_emails.  
This  function  opens and reads the content of the CSV file. 
Each email must be in its line. 
Here is an example of how the emails must be saved: 
jj@gmail.com 
kate@yahoo.com 
  
and not like this : 
jj@gmail.comkate@yahoo.com """

import pandas as pd

def save_emails():
    emails = []
    while True:
        email = input("Please enter an email id or done to finish: ")
        
        if email.lower() == 'done':
            break

        emails.append(email)

    df = pd.DataFrame(emails, columns=["Email"])
    df.to_csv('emails.csv', index=False)
    return "Emails entered successfully"

def open_emails():
    df = pd.read_csv("emails.csv")
    return df['Email'].values

print(save_emails())
print(open_emails())