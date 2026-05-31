"""
Enrollment Management Module
Handles enrollment operations
"""

from db_connection import DatabaseConnection
from datetime import datetime

class Enrollment:
    """Manages enrollment operations"""
    
    def __init__(self):
        """Initialize enrollment manager with database connection"""
        self.db = DatabaseConnection()
    
    def enroll_student(self, student_id, course_id, enrollment_date=None):
        """
        Enroll a student in a course
        
        Args:
            student_id: Student ID
            course_id: Course ID
            enrollment_date: Enrollment date (YYYY-MM-DD), defaults to today
            
        Returns:
            Boolean indicating success/failure
        """
        # Use current date if not provided
        if enrollment_date is None:
            enrollment_date = datetime.now().strftime('%Y-%m-%d')
        
        # Validate inputs
        if not self._student_exists(student_id):
            print(f"Error: Student with ID {student_id} not found.")
            return False
        
        if not self._course_exists(course_id):
            print(f"Error: Course with ID {course_id} not found.")
            return False
        
        # Check if student is already enrolled
        query = "SELECT enrollment_id FROM enrollments WHERE student_id = %s AND course_id = %s"
        if self.db.fetch_one(query, (student_id, course_id)):
            print(f"Error: Student {student_id} is already enrolled in course {course_id}.")
            return False
        
        # Insert enrollment
        query = """INSERT INTO enrollments (student_id, course_id, enrollment_date) 
                   VALUES (%s, %s, %s)"""
        
        if self.db.execute_query(query, (student_id, course_id, enrollment_date)):
            print(f"✓ Student {student_id} enrolled in course {course_id} successfully.")
            return True
        else:
            print("Error: Failed to enroll student.")
            return False
    
    def remove_enrollment(self, enrollment_id):
        """
        Remove an enrollment
        
        Args:
            enrollment_id: Enrollment ID to remove
            
        Returns:
            Boolean indicating success/failure
        """
        if not self._enrollment_exists(enrollment_id):
            print(f"Error: Enrollment with ID {enrollment_id} not found.")
            return False
        
        query = "DELETE FROM enrollments WHERE enrollment_id = %s"
        
        if self.db.execute_query(query, (enrollment_id,)):
            print(f"✓ Enrollment {enrollment_id} removed successfully.")
            return True
        else:
            print("Error: Failed to remove enrollment.")
            return False
    
    def get_student_courses(self, student_id):
        """
        Get all courses for a student
        
        Args:
            student_id: Student ID
            
        Returns:
            List of courses or None
        """
        if not self._student_exists(student_id):
            print(f"Error: Student with ID {student_id} not found.")
            return None
        
        query = """SELECT c.course_id, c.course_name, c.credits, e.enrollment_date, e.grade
                   FROM enrollments e
                   JOIN courses c ON e.course_id = c.course_id
                   WHERE e.student_id = %s
                   ORDER BY e.enrollment_date DESC"""
        
        return self.db.fetch_query(query, (student_id,))
    
    def get_course_students(self, course_id):
        """
        Get all students enrolled in a course
        
        Args:
            course_id: Course ID
            
        Returns:
            List of students or None
        """
        if not self._course_exists(course_id):
            print(f"Error: Course with ID {course_id} not found.")
            return None
        
        query = """SELECT s.student_id, s.first_name, s.last_name, s.email, e.enrollment_date, e.grade
                   FROM enrollments e
                   JOIN students s ON e.student_id = s.student_id
                   WHERE e.course_id = %s
                   ORDER BY s.first_name"""
        
        return self.db.fetch_query(query, (course_id,))
    
    def get_all_enrollments(self):
        """
        Get all enrollments
        
        Returns:
            List of all enrollments or None
        """
        query = """SELECT e.enrollment_id, s.student_id, s.first_name, s.last_name,
                          c.course_id, c.course_name, e.enrollment_date, e.grade
                   FROM enrollments e
                   JOIN students s ON e.student_id = s.student_id
                   JOIN courses c ON e.course_id = c.course_id
                   ORDER BY e.enrollment_date DESC"""
        
        return self.db.fetch_query(query)
    
    def update_grade(self, enrollment_id, grade):
        """
        Update student grade for a course
        
        Args:
            enrollment_id: Enrollment ID
            grade: Grade (A, B, C, D, F, etc.)
            
        Returns:
            Boolean indicating success/failure
        """
        if not self._enrollment_exists(enrollment_id):
            print(f"Error: Enrollment with ID {enrollment_id} not found.")
            return False
        
        query = "UPDATE enrollments SET grade = %s WHERE enrollment_id = %s"
        
        if self.db.execute_query(query, (grade, enrollment_id)):
            print(f"✓ Grade updated successfully.")
            return True
        else:
            print("Error: Failed to update grade.")
            return False
    
    def _student_exists(self, student_id):
        """Check if student exists"""
        query = "SELECT student_id FROM students WHERE student_id = %s"
        return self.db.fetch_one(query, (student_id,)) is not None
    
    def _course_exists(self, course_id):
        """Check if course exists"""
        query = "SELECT course_id FROM courses WHERE course_id = %s"
        return self.db.fetch_one(query, (course_id,)) is not None
    
    def _enrollment_exists(self, enrollment_id):
        """Check if enrollment exists"""
        query = "SELECT enrollment_id FROM enrollments WHERE enrollment_id = %s"
        return self.db.fetch_one(query, (enrollment_id,)) is not None
    
    def display_enrollment(self, enrollment):
        """Display enrollment information in formatted way"""
        print(f"\n{'='*60}")
        print(f"Enrollment ID: {enrollment[0]}")
        print(f"Student: {enrollment[2]} {enrollment[3]} (ID: {enrollment[1]})")
        print(f"Course: {enrollment[5]} (ID: {enrollment[4]})")
        print(f"Enrollment Date: {enrollment[6]}")
        print(f"Grade: {enrollment[7] if len(enrollment) > 7 else 'Not Graded'}")
        print(f"{'='*60}")
    
    def close_connection(self):
        """Close database connection"""
        self.db.close_connection()