from university import University
from student import Student

# Demonstrating the implementation
if __name__ == "__main__":
    # Initialize university and students
    university = University("Tech University")
    students = [Student(f"Student {i}") for i in range(7)]

    # Students apply to the university
    for student in students:
        university.apply(student)

    # Process applications
    university.process_applications()