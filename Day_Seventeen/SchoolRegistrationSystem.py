# Student Grade Management System

# ----------------------------
# Data Structures Initialization
# ----------------------------

# Lists: Used to store an ordered collection of items. Lists are mutable (can be modified).
# Use lists when you need to store multiple items in a specific order and may need to add, remove, or modify items.
# Example: Storing a list of students.
students = []  # List to store student tuples (name, grades)

# Sets: Used to store unique, unordered items. Sets are mutable but do not allow duplicate values.
# Use sets when you need to ensure all items are unique or perform operations like union, intersection, etc.
# Example: Storing unique subjects across all students.
subjects = set()  # Set to store unique subjects

# Dictionaries: Used to store key-value pairs. Dictionaries are mutable and allow fast lookups by key.
# Use dictionaries when you need to map unique keys to values, like a phone book or database.
# Example: Mapping student names to their grades for quick access.
grades_dict = {}  # Dictionary to map student names to their grades

# Tuples: Used to store an ordered, immutable collection of items. Tuples are faster than lists but cannot be modified.
# Use tuples when you have a fixed collection of items that should not change, like coordinates or student records.
# Example: Storing student details (name, grades) as a tuple.

# ----------------------------
# Functions
# ----------------------------

def add_student():
    """
    Adds a student and their grades to the system.
    Uses lists, tuples, sets, and dictionaries.
    """
    name = input("Enter student name: ")
    grades = []  # List to store tuples of (subject, grade)
    
    print("Enter grades for each subject (type 'done' to finish):")
    while True:
        subject = input("Enter subject: ") #English
        if subject.lower() == 'done':       #done
            break
        grade = float(input(f"Enter grade for {subject}: ")) #enter grade for english
        # -->98
        
        # Tuples: Store (subject, grade) as a tuple because it's a fixed pair of values.
        grades.append((subject, grade))  # Add tuple to the grades list
        #output-->English, 98.00
        # Sets: Add the subject to the set to ensure it's unique.
        subjects.add(subject)  # Add subject to the set
        # subjects = set() -->  subjects = set(English)
    
    # Lists: Append the student tuple (name, grades) to the students list.
    students.append((name, grades))  # Add student tuple to the list
    
    # Dictionaries: Map the student name to their grades for quick lookup.
    grades_dict[name] = grades  # Add student to the dictionary
    
    print(f"Student {name} added successfully!\n")

def view_students():
    """
    Displays all students and their grades.
    Uses lists and tuples.
    """
    if not students:
        print("No students found.\n")
        return
    
    print("Students and their grades:")
    for name, grades in students:  # Iterate through the list of student tuples
        print(f"{name}:")
        for subject, grade in grades:  # Iterate through the list of grade tuples
            print(f"  {subject}: {grade}")
    print()

def calculate_average(name):
    """
    Calculates the average grade for a specific student.
    Uses dictionaries and lists.
    """
    if name not in grades_dict:
        print(f"Student {name} not found.\n")
        return
    
    # Dictionaries: Retrieve the grades for the student using their name as the key.
    grades = grades_dict[name]
    
    # Lists: Use a list comprehension to extract grades from the list of tuples.
    total = sum(grade for _, grade in grades)  # Sum all grades
    average = total / len(grades)  # Calculate average
    
    print(f"Average grade for {name}: {average:.2f}\n")

def find_highest_lowest():
    """
    Finds the highest and lowest grades in the class.
    Uses dictionaries and lists.
    """
    if not students:
        print("No students found.\n")
        return
    
    # Lists: Use a list comprehension to flatten all grades into a single list.
    all_grades = [grade for grades in grades_dict.values() for _, grade in grades]
    
    # Built-in functions: Use max() and min() to find the highest and lowest grades.
    highest = max(all_grades)
    lowest = min(all_grades)
    
    print(f"Highest grade in class: {highest}")
    print(f"Lowest grade in class: {lowest}\n")

def remove_student():
    """
    Removes a student from the system.
    Uses lists and dictionaries.
    """
    name = input("Enter student name to remove: ")
    if name not in grades_dict:
        print(f"Student {name} not found.\n")
        return
    
    # Lists: Use a list comprehension to filter out the student.
    students[:] = [student for student in students if student[0] != name]  # Remove from list
    
    # Dictionaries: Use the del keyword to remove the student from the dictionary.
    del grades_dict[name]  # Remove from dictionary
    
    print(f"Student {name} removed successfully!\n")

# ----------------------------
# Main Menu
# ----------------------------

def main_menu():
    """
    Displays the main menu and handles user input.
    """
    while True:
        print("Student Grade Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Calculate Average Grade")
        print("4. Find Highest and Lowest Grades")
        print("5. Remove Student")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            name = input("Enter student name: ")
            calculate_average(name)
        elif choice == '4':
            find_highest_lowest()
        elif choice == '5':
            remove_student()
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# ----------------------------
# Run the Program
# ----------------------------

# Start the program by calling the main menu function.
main_menu()