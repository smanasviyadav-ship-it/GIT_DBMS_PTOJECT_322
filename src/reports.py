"""
Reports Module
Generates various reports for the system
"""

from db_connection import DatabaseConnection

class Reports:
    """Generates system reports"""
    
    def __init__(self):
        """Initialize reports with database connection"""
        self.db = DatabaseConnection()
    
    def total_students(self):
        """
        Get total number of students
        
        Returns:
            Integer count
        """
        query = "SELECT COUNT(*) FROM students"
        result = self.db.fetch_one(query)
        return result[0] if result else 0
    
    def total_courses(self):
        """
        Get total number of courses
        
        Returns:
            Integer count
        """
        query = "SELECT COUNT(*) FROM courses"
        result = self.db.fetch_one(query)
        return result[0] if result else 0
    
    def total_enrollments(self):
        """
        Get total number of enrollments
        
        Returns:
            Integer count
        """
        query = "SELECT COUNT(*) FROM enrollments"
        result = self.db.fetch_one(query)
        return result[0] if result else 0
    
    def students_per_course(self):
        """
        Get number of students per course
        
        Returns:
            List of (course_name, student_count) tuples
        """
        query = """SELECT c.course_name, COUNT(e.enrollment_id) as student_count
                   FROM courses c
                   LEFT JOIN enrollments e ON c.course_id = e.course_id
                   GROUP BY c.course_id, c.course_name
                   ORDER BY student_count DESC"""
        
        return self.db.fetch_query(query)
    
    def courses_per_student(self):
        """
        Get number of courses per student
        
        Returns:
            List of (student_name, course_count) tuples
        """
        query = """SELECT CONCAT(s.first_name, ' ', s.last_name) as student_name, 
                          COUNT(e.enrollment_id) as course_count
                   FROM students s
                   LEFT JOIN enrollments e ON s.student_id = e.student_id
                   GROUP BY s.student_id
                   ORDER BY course_count DESC"""
        
        return self.db.fetch_query(query)
    
    def enrollment_summary(self):
        """
        Get detailed enrollment summary
        
        Returns:
            List of enrollment details
        """
        query = """SELECT e.enrollment_id,
                          CONCAT(s.first_name, ' ', s.last_name) as student_name,
                          c.course_name,
                          e.enrollment_date,
                          e.grade
                   FROM enrollments e
                   JOIN students s ON e.student_id = s.student_id
                   JOIN courses c ON e.course_id = c.course_id
                   ORDER BY e.enrollment_date DESC"""
        
        return self.db.fetch_query(query)
    
    def student_performance_summary(self):
        """
        Get student performance summary
        
        Returns:
            List of (student_name, total_courses, grades)
        """
        query = """SELECT CONCAT(s.first_name, ' ', s.last_name) as student_name,
                          COUNT(e.enrollment_id) as total_courses,
                          GROUP_CONCAT(e.grade SEPARATOR ', ') as grades
                   FROM students s
                   LEFT JOIN enrollments e ON s.student_id = e.student_id
                   GROUP BY s.student_id
                   ORDER BY student_name"""
        
        return self.db.fetch_query(query)
    
    def course_popularity(self):
        """
        Get course popularity (sorted by enrollment count)
        
        Returns:
            List of (course_name, credits, enrollment_count)
        """
        query = """SELECT c.course_name, c.credits, COUNT(e.enrollment_id) as enrollment_count
                   FROM courses c
                   LEFT JOIN enrollments e ON c.course_id = e.course_id
                   GROUP BY c.course_id, c.course_name, c.credits
                   ORDER BY enrollment_count DESC"""
        
        return self.db.fetch_query(query)
    
    def print_system_summary(self):
        """Print complete system summary"""
        print("\n" + "="*70)
        print(" "*20 + "SYSTEM SUMMARY REPORT")
        print("="*70)
        
        print(f"\nTotal Students: {self.total_students()}")
        print(f"Total Courses: {self.total_courses()}")
        print(f"Total Enrollments: {self.total_enrollments()}")
        
        print("\n" + "-"*70)
        print("STUDENTS PER COURSE")
        print("-"*70)
        
        courses_data = self.students_per_course()
        if courses_data:
            for course_name, student_count in courses_data:
                print(f"  {course_name}: {student_count} students")
        else:
            print("  No data available")
        
        print("\n" + "-"*70)
        print("COURSES PER STUDENT")
        print("-"*70)
        
        students_data = self.courses_per_student()
        if students_data:
            for student_name, course_count in students_data:
                print(f"  {student_name}: {course_count} courses")
        else:
            print("  No data available")
        
        print("\n" + "-"*70)
        print("COURSE POPULARITY")
        print("-"*70)
        
        popularity = self.course_popularity()
        if popularity:
            for course_name, credits, enrollment_count in popularity:
                print(f"  {course_name} ({credits} credits): {enrollment_count} enrollments")
        else:
            print("  No data available")
        
        print("\n" + "="*70 + "\n")
    
    def print_enrollment_summary(self):
        """Print detailed enrollment summary"""
        print("\n" + "="*80)
        print(" "*20 + "ENROLLMENT SUMMARY REPORT")
        print("="*80)
        
        data = self.enrollment_summary()
        if data:
            print(f"\n{'ID':<5} {'Student Name':<25} {'Course Name':<30} {'Date':<12} {'Grade':<6}")
            print("-"*80)
            
            for record in data:
                enrollment_id, student_name, course_name, enrollment_date, grade = record
                grade_display = grade if grade else "N/A"
                print(f"{enrollment_id:<5} {student_name:<25} {course_name:<30} {str(enrollment_date):<12} {grade_display:<6}")
        else:
            print("\nNo enrollment data available")
        
        print("\n" + "="*80 + "\n")
    
    def close_connection(self):
        """Close database connection"""
        self.db.close_connection()