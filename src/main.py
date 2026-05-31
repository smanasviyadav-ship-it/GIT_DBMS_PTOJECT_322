"""
Student Management System - Main Application
Entry point for the system
"""

from student import Student
from course import Course
from enrollment import Enrollment
from reports import Reports
from db_connection import DatabaseConnection

def print_menu():
    """Print main menu options"""
    print("\n" + "="*60)
    print(" "*15 + "STUDENT MANAGEMENT SYSTEM")
    print("="*60)
    print("\n1.  Student Management")
    print("2.  Course Management")
    print("3.  Enrollment Management")
    print("4.  View Reports")
    print("5.  Exit")
    print("-"*60)

def student_menu():
    """Student management submenu"""
    student_manager = Student()
    
    while True:
        print("\n--- STUDENT MANAGEMENT ---")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. View All Students")
        print("6. Back to Main Menu")
        print("-"*40)
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            print("\n--- ADD STUDENT ---")
            first_name = input("First Name: ").strip()
            last_name = input("Last Name: ").strip()
            gender = input("Gender (Male/Female/Other): ").strip()
            dob = input("Date of Birth (YYYY-MM-DD): ").strip()
            email = input("Email: ").strip()
            phone = input("Phone: ").strip()
            
            student_manager.add_student(first_name, last_name, gender, dob, email, phone)
        
        elif choice == '2':
            print("\n--- UPDATE STUDENT ---")
            student_id = int(input("Enter Student ID to update: "))
            print("Enter fields to update (leave blank to skip):")
            first_name = input("First Name: ").strip() or None
            last_name = input("Last Name: ").strip() or None
            gender = input("Gender: ").strip() or None
            dob = input("Date of Birth (YYYY-MM-DD): ").strip() or None
            email = input("Email: ").strip() or None
            phone = input("Phone: ").strip() or None
            
            student_manager.update_student(student_id, first_name, last_name, gender, dob, email, phone)
        
        elif choice == '3':
            print("\n--- DELETE STUDENT ---")
            student_id = int(input("Enter Student ID to delete: "))
            confirm = input("Are you sure? (yes/no): ").strip().lower()
            if confirm == 'yes':
                student_manager.delete_student(student_id)
        
        elif choice == '4':
            print("\n--- SEARCH STUDENT ---")
            print("1. Search by ID")
            print("2. Search by Name")
            print("3. Search by Email")
            search_choice = input("Select search type (1-3): ").strip()
            
            if search_choice == '1':
                student_id = int(input("Enter Student ID: "))
                results = student_manager.search_student('id', student_id)
            elif search_choice == '2':
                name = input("Enter Name: ").strip()
                results = student_manager.search_student('name', name)
            elif search_choice == '3':
                email = input("Enter Email: ").strip()
                results = student_manager.search_student('email', email)
            else:
                print("Invalid choice")
                continue
            
            if results:
                for student in results:
                    student_manager.display_student(student)
            else:
                print("No students found.")
        
        elif choice == '5':
            print("\n--- ALL STUDENTS ---")
            students = student_manager.get_all_students()
            if students:
                for student in students:
                    student_manager.display_student(student)
            else:
                print("No students found.")
        
        elif choice == '6':
            break
        
        else:
            print("Invalid choice. Please try again.")
    
    student_manager.close_connection()

def course_menu():
    """Course management submenu"""
    course_manager = Course()
    
    while True:
        print("\n--- COURSE MANAGEMENT ---")
        print("1. Add Course")
        print("2. Update Course")
        print("3. Delete Course")
        print("4. Search Course")
        print("5. View All Courses")
        print("6. Back to Main Menu")
        print("-"*40)
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            print("\n--- ADD COURSE ---")
            course_name = input("Course Name: ").strip()
            credits = int(input("Credits: "))
            description = input("Description: ").strip()
            
            course_manager.add_course(course_name, credits, description)
        
        elif choice == '2':
            print("\n--- UPDATE COURSE ---")
            course_id = int(input("Enter Course ID to update: "))
            print("Enter fields to update (leave blank to skip):")
            course_name = input("Course Name: ").strip() or None
            credits_input = input("Credits: ").strip()
            credits = int(credits_input) if credits_input else None
            description = input("Description: ").strip() or None
            
            course_manager.update_course(course_id, course_name, credits, description)
        
        elif choice == '3':
            print("\n--- DELETE COURSE ---")
            course_id = int(input("Enter Course ID to delete: "))
            confirm = input("Are you sure? (yes/no): ").strip().lower()
            if confirm == 'yes':
                course_manager.delete_course(course_id)
        
        elif choice == '4':
            print("\n--- SEARCH COURSE ---")
            print("1. Search by ID")
            print("2. Search by Name")
            search_choice = input("Select search type (1-2): ").strip()
            
            if search_choice == '1':
                course_id = int(input("Enter Course ID: "))
                results = course_manager.search_course('id', course_id)
            elif search_choice == '2':
                name = input("Enter Course Name: ").strip()
                results = course_manager.search_course('name', name)
            else:
                print("Invalid choice")
                continue
            
            if results:
                for course in results:
                    course_manager.display_course(course)
            else:
                print("No courses found.")
        
        elif choice == '5':
            print("\n--- ALL COURSES ---")
            courses = course_manager.get_all_courses()
            if courses:
                for course in courses:
                    course_manager.display_course(course)
            else:
                print("No courses found.")
        
        elif choice == '6':
            break
        
        else:
            print("Invalid choice. Please try again.")
    
    course_manager.close_connection()

def enrollment_menu():
    """Enrollment management submenu"""
    enrollment_manager = Enrollment()
    
    while True:
        print("\n--- ENROLLMENT MANAGEMENT ---")
        print("1. Enroll Student in Course")
        print("2. Remove Enrollment")
        print("3. View Student's Courses")
        print("4. View Students in Course")
        print("5. View All Enrollments")
        print("6. Update Grade")
        print("7. Back to Main Menu")
        print("-"*40)
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == '1':
            print("\n--- ENROLL STUDENT ---")
            student_id = int(input("Enter Student ID: "))
            course_id = int(input("Enter Course ID: "))
            enrollment_date = input("Enrollment Date (YYYY-MM-DD) [leave blank for today]: ").strip()
            enrollment_date = enrollment_date if enrollment_date else None
            
            enrollment_manager.enroll_student(student_id, course_id, enrollment_date)
        
        elif choice == '2':
            print("\n--- REMOVE ENROLLMENT ---")
            enrollment_id = int(input("Enter Enrollment ID to remove: "))
            confirm = input("Are you sure? (yes/no): ").strip().lower()
            if confirm == 'yes':
                enrollment_manager.remove_enrollment(enrollment_id)
        
        elif choice == '3':
            print("\n--- VIEW STUDENT'S COURSES ---")
            student_id = int(input("Enter Student ID: "))
            courses = enrollment_manager.get_student_courses(student_id)
            if courses:
                print(f"\nCourses for Student {student_id}:")
                for course in courses:
                    print(f"  - {course[1]} ({course[2]} credits) | Enrolled: {course[3]} | Grade: {course[4] if course[4] else 'N/A'}")
            else:
                print("No courses found for this student.")
        
        elif choice == '4':
            print("\n--- VIEW STUDENTS IN COURSE ---")
            course_id = int(input("Enter Course ID: "))
            students = enrollment_manager.get_course_students(course_id)
            if students:
                print(f"\nStudents in Course {course_id}:")
                for student in students:
                    print(f"  - {student[1]} {student[2]} ({student[3]}) | Enrolled: {student[4]} | Grade: {student[5] if student[5] else 'N/A'}")
            else:
                print("No students found in this course.")
        
        elif choice == '5':
            print("\n--- ALL ENROLLMENTS ---")
            enrollments = enrollment_manager.get_all_enrollments()
            if enrollments:
                for enrollment in enrollments:
                    enrollment_manager.display_enrollment(enrollment)
            else:
                print("No enrollments found.")
        
        elif choice == '6':
            print("\n--- UPDATE GRADE ---")
            enrollment_id = int(input("Enter Enrollment ID: "))
            grade = input("Enter Grade (A, B, C, D, F, etc.): ").strip().upper()
            enrollment_manager.update_grade(enrollment_id, grade)
        
        elif choice == '7':
            break
        
        else:
            print("Invalid choice. Please try again.")
    
    enrollment_manager.close_connection()

def reports_menu():
    """Reports submenu"""
    reports = Reports()
    
    while True:
        print("\n--- REPORTS ---")
        print("1. System Summary")
        print("2. Enrollment Summary")
        print("3. Students Per Course")
        print("4. Courses Per Student")
        print("5. Course Popularity")
        print("6. Student Performance Summary")
        print("7. Back to Main Menu")
        print("-"*40)
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == '1':
            reports.print_system_summary()
        
        elif choice == '2':
            reports.print_enrollment_summary()
        
        elif choice == '3':
            data = reports.students_per_course()
            if data:
                print("\n--- STUDENTS PER COURSE ---")
                for course_name, student_count in data:
                    print(f"{course_name}: {student_count} students")
            else:
                print("No data available")
        
        elif choice == '4':
            data = reports.courses_per_student()
            if data:
                print("\n--- COURSES PER STUDENT ---")
                for student_name, course_count in data:
                    print(f"{student_name}: {course_count} courses")
            else:
                print("No data available")
        
        elif choice == '5':
            data = reports.course_popularity()
            if data:
                print("\n--- COURSE POPULARITY ---")
                for course_name, credits, enrollment_count in data:
                    print(f"{course_name} ({credits} credits): {enrollment_count} enrollments")
            else:
                print("No data available")
        
        elif choice == '6':
            data = reports.student_performance_summary()
            if data:
                print("\n--- STUDENT PERFORMANCE SUMMARY ---")
                for student_name, total_courses, grades in data:
                    print(f"{student_name}: {total_courses} courses | Grades: {grades if grades else 'N/A'}")
            else:
                print("No data available")
        
        elif choice == '7':
            break
        
        else:
            print("Invalid choice. Please try again.")
    
    reports.close_connection()

def main():
    """Main application loop"""
    print("\n" + "="*60)
    print(" "*10 + "Welcome to Student Management System")
    print("="*60)
    
    # Test database connection
    db = DatabaseConnection()
    if not db.is_connected():
        print("\n✗ Error: Cannot connect to database.")
        print("Please ensure MySQL is running and the database is configured correctly.")
        print("Check your .env file for correct credentials.")
        db.close_connection()
        return
    
    db.close_connection()
    print("✓ Database connection successful!\n")
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            student_menu()
        elif choice == '2':
            course_menu()
        elif choice == '3':
            enrollment_menu()
        elif choice == '4':
            reports_menu()
        elif choice == '5':
            print("\nThank you for using Student Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()