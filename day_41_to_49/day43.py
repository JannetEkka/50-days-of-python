"""Day 43: Student Marks 
 
Write a function called student_marks that records marks achieved by students in a test. 
The function should ask the user to input the name  of  the  student  
and  then  ask  the  user  to  input  the  marks achieved  by  the  student.  
The  information  should  be  stored  in  a dictionary. 
The name is the key and the marks are the value. 
When the  user  enters  done,  
the  function  should  return  a  dictionary  of names and values entered. """

def student_marks():
    stu_dict = {}

    while True:    
        name = input("Enter student name(or 'done' to finish): ")

        if name.lower() == 'done':
            return stu_dict
        try:
            marks = float(input(f"Enter marks achieved by {name}: "))
            stu_dict[name] = marks
        except ValueError:
            print("Enter valid number for marks!")
            continue

print(student_marks())