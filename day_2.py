"""
 Challenge: Student Marks Analyzer

Create a Python program that allows a user to input student names along with their marks and then calculates useful statistics.

Your program should:
1. Let the user input multiple students with their marks (name + integer score).
2. After input is complete, display:
   - Average marks
   - Highest marks and student(s) who scored it
   - Lowest marks and student(s) who scored it
   - Total number of students

Bonus:
- Allow the user to enter all data first, then view the report
- Format output clearly in a report-style layout
- Prevent duplicate student names
"""

def collect_data():
    students = {}

    while True:
          name = input("Enter the name of the student or done to exit : ").strip()
      
          if name.lower() == "done":
              break

          if name in students:
            print("Student name already exists")
            continue

          try:
            marks = float(input(f"Enter the marks for {name} : "))
            students[name] = marks
          except ValueError:
            print("Enter a valid number for marks")

    return students

def display_data(student):
   if not student:
      print("No student data found!")
      return

   marks = list(students.values())
   max_score = max(marks)
   min_score = min(marks)
   average = sum(marks) / len(marks)

   topper = [name for name, score in students.items() if score == max_score ]
   bottomer = [name for name, score in students.items() if score == min_score ]

   print("\n Students marks report 🗓️")
   print("-" * 30)
   print(f"Total students: {len(students)}")
   print(f"average marks for students: {average:.2f}")
   print(f"Highest marks : {max_score} by {', '.join(topper)}")
   print(f"lowest marks : {min_score} by {', '.join(bottomer)}")

   print("-" * 30)
   print("Detailed Marks 🗓️")
   for name, score in students.items():
        print(f" - {name}: {score}")


students = collect_data()
display_data(students)