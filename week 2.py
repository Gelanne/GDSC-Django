import json

student = {}

def add_student(name, age, grade):
    """Adds a new student to the database
    Args:
       name: The student"s name.
       age: The student"s age.
       grade: The student"s grade.
       """
    
    student = {
        "name": name,
        "age": age,
        "grade": grade
    }

    students[name] = student


def view_student(name):
        """Views the details of a specific student.
        
        Args:
          name: The student"s name.
          """
        
        if name not in students:
            print("The student does not exist.")
            return
        
        print("Name:", students[name]["name"])
        print("Age:", student[name]["age"])
        print("Grade:", students[name]["grade"])



def list_students():
    """Lists all students in the database."""

    for name in students:
      print(name)


def update_student(name, age, grade):
    """Updates the information of a specific student.
    
    Args:
     name: The student's name.
     age: The student's age.
     grade: The stuednt's grade.
     """
    
  if name not in students:
    print("The student does not exist")
    return

 students[name]["age"] = age
 students[name]["grade"] = grade


def delete_students(name):
    """Deletes a student from the database.
    
    Args:
     name: The student's name.
     """
    
    if name not in students:
        print("The student does not exist.")
    return

 del students[name]


choice = input("What woud you like to do?\n"
            "1.Add a student\n"
            "2.View a student\n"
            "3.List all student\n"
            "4.Update a student\n"
            "5.Deletes a student\n"
            "6.Quit\n")

while choice !="6":
    if choice == "1":
        name = input("Enter the student's name: ")
        age = input("Enter the student's age: ")
        grade = input("Enter the student's grade: ")

        add_student(name, age, grade)
    
    elif choice == "2":
        name = input("Enter the student's name: ")

        view_student(name)

    elif choice == "3":
        list_students()

    elif choice == "4":
        name = input("Enter the student's name: ")
        age = input("Enter the student's age: ")
        grade = input("Enter the student's grade: ")

        update_student(name, age, grade)

    elif choice == "5":
        name = input("Enter the student's name: ")

        del_student[name] 
