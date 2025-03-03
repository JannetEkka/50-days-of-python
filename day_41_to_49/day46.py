"""Day 46: Create a DataFrame 
 
Create a Dataframe using pandas. 
You are going to create a code to put the following into a Dataframe. 
You will use the information in the table below. 
Basically, you are going to recreate this table using pandas. 
Use the information in the table to recreate the table. 
year    Title       genre 
2009    Brothers    Drama 
2002    Spider-Man  Sci-fi 
2009    WatchMen    Drama 
2010    Inception   Sci-fi 
2009    Avatar      Fantasy"""
  
import pandas as pd

movies_dict = {'year':['2009', '2002', '2009', '2010', '2009'],
               'Title':['Brothers', 'Spider-Man', 'WatchMen', 'Inception', 'Avatar'],
               'genre':['Drama', 'Sci-fi', 'Drama', 'Sci-fi', 'Fantasy']}

df = pd.DataFrame(movies_dict)
print(df)