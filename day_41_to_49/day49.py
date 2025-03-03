"""Day 49: Create a Database 
 
For  this  challenge,  you  are  going  to  create  a  database  using Python’s SQLite. 
You will import SQLite into your script. 
Create a database  called  movies.db.  
In  that  database,  you  are  going  to create a table called movies. 
In that table, you are going to save the following movies: 
 
year title genre 
2009 Brothers Drama 
2002 Spider Man Sci-fi 
2009 WatchMen Drama 
2010 Inception Sci-fi 
2009 Avatar Fantasy 
 
a)  Once  you  create  a  table,  run  a  SQL  query  to  see  all  the movies in your table. 
b)  Run  another  SQL  query  to  select  only  the  movie  Brothers from the list. 
c)  Run  another  SQL  query  to  select  all  movies  that  were released in 2009 from your table. 
d)  Run another query to select movies in the fantasy and drama genre. 
e)  Run a query to delete all the contents of your table.
"""
import sqlite3

conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS movies")

cursor.execute('''
CREATE TABLE movies (
    year INTEGER,
    title TEXT,
    genre TEXT          
)
''')

movies = [
    (2009, "Brothers", "Drama"),
    (2002, "Spider Man", "Sci-fi"),
    (2009, "WatchMen", "Drama"),
    (2010, "Inception", "Sci-fi"),
    (2009, "Avatar", "Fantasy")
]

cursor.executemany("INSERT INTO movies (year, title, genre) VALUES (?,?,?)", movies)
conn.commit()

print("All movies in table:\n")
cursor.execute("SELECT * FROM movies")
print(cursor.fetchall())

print("\nOnly Brothers in table:\n")
cursor.execute("SELECT * FROM movies WHERE title= 'Brothers'")
print(cursor.fetchall())

print("\nMovies from 2009:\n")
cursor.execute("SELECT title FROM movies WHERE year = 2009")
print(cursor.fetchall())

print("\nFantasy and Drama Movies:\n")
cursor.execute("SELECT * FROM movies WHERE genre IN ('Fantasy','Drama')")
print(cursor.fetchall())

cursor.execute("DELETE FROM movies")
conn.commit()
print("\nAll records deleted.")

conn.close()