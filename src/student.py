"""
Student Management Module
Handles student CRUD operations
"""

from db_connection import DatabaseConnection
from datetime import datetime
import re

class Student:
    """Manages student operations"""
    
    def __init__(self):
        """Initialize student manager with database connection"""
        self.db = DatabaseConnection()
    
    @staticmethod
    def validate_email(email):
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def validate_phone(phone):
        """Validate phone number format"""
        pattern = r'^[\d\s\-\+\(\)]{10,}$'
        return re.match(pattern, phone) is not None
    
    @staticmethod
    def validate_date(date_string):
        """Validate date format (YYYY-MM-DD)"""
        try:
            datetime.strptime(date_string, '%Y-%m-%d')
            return True
        except ValueError:
            return False
    
    def add_student(self, first_name, last_name, gender, date_of_birth, email, phone):
        """
        Add a new student
        
        Args:
            first_name: Student's first name
            last_name: Student's last name
            gender: Student's gender
            date_of_birth: Student's date of birth (YYYY-MM-DD)
            email: Student's email (must be unique)
            phone: Student's phone number
            
        Returns:
            Boolean indicating success/failure
        """
        # Input validation
        if not first_name or not last_name:
            print("Error: First name and last name are required.")
            return False
        
        if not self.validate_email(email):
            print("Error: Invalid email format.")
            return False
        
        if not self.validate_phone(phone):
            print("Error: Invalid phone format.")
            return False
        
        if not self.validate_date(date_of_birth):
            print("Error: Invalid date format. Use YYYY-MM-DD.")
            return False
        
        # Check if email already exists
        query = "SELECT student_id FROM students WHERE email = %s"
        if self.db.fetch_one(query, (email,)):
            print(f"Error: Email '{email}' already exists.")
            return False
        
        # Insert student
        query = """INSERT INTO students 
                   (first_name, last_name, gender, date_of_birth, email, phone) 
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        
        if self.db.execute_query(query, (first_name, last_name, gender, date_of_birth, email, phone)):
            print(f"✓ Student '{first_name} {last_name}' added successfully.")
            return True
        else:
            print("Error: Failed to add student.")
            return False
    
    def update_student(self, student_id, first_name=None, last_name=None, gender=None, 
                      date_of_birth=None, email=None, phone=None):
        """
        Update student information
        
        Args:
            student_id: Student ID to update
            Other args: Fields to update (None means no change)
            
        Returns:
            Boolean indicating success/failure
        """
        # Check if student exists
        if not self._student_exists(student_id):
            print(f"Error: Student with ID {student_id} not found.")
            return False
        
        # Build update query dynamically
        updates = []
        params = []
        
        if first_name:
            updates.append("first_name = %s")
            params.append(first_name)
        
        if last_name:
            updates.append("last_name = %s")
            params.append(last_name)
        
        if gender:
            updates.append("gender = %s")
            params.append(gender)
        
        if date_of_birth:
            if not self.validate_date(date_of_birth):
                print("Error: Invalid date format. Use YYYY-MM-DD.")
                return False
            updates.append("date_of_birth = %s")
            params.append(date_of_birth)
        
        if email:
            if not self.validate_email(email):
                print("Error: Invalid email format.")
                return False
            # Check if email is unique
            query = "SELECT student_id FROM students WHERE email = %s AND student_id != %s"
            if self.db.fetch_one(query, (email, student_id)):
                print(f"Error: Email '{email}' already exists.")
                return False
            updates.append("email = %s")
            params.append(email)
        
        if phone:
            if not self.validate_phone(phone):
                print("Error: Invalid phone format.")
                return False
            updates.append("phone = %s")
            params.append(phone)
        
        if not updates:
            print("Error: No fields to update.")
            return False
        
        params.append(student_id)
        query = f"UPDATE students SET {', '.join(updates)} WHERE student_id = %s"
        
        if self.db.execute_query(query, params):
            print(f"✓ Student ID {student_id} updated successfully.")
            return True
        else:
            print("Error: Failed to update student.")
            return False
    
    def delete_student(self, student_id):
        """
        Delete a student
        
        Args:
            student_id: Student ID to delete
            
        Returns:
            Boolean indicating success/failure
        """
        if not self._student_exists(student_id):
            print(f"Error: Student with ID {student_id} not found.")
            return False
        
        query = "DELETE FROM students WHERE student_id = %s"
        
        if self.db.execute_query(query, (student_id,)):
            print(f"✓ Student ID {student_id} deleted successfully.")
            return True
        else:
            print("Error: Failed to delete student.")
            return False
    
    def search_student(self, search_type, search_value):
        """
        Search for students
        
        Args:
            search_type: 'id', 'name', or 'email'
            search_value: Value to search for
            
        Returns:
            List of matching students or None
        """
        if search_type == 'id':
            query = "SELECT * FROM students WHERE student_id = %s"
            results = self.db.fetch_query(query, (search_value,))
        
        elif search_type == 'name':
            query = "SELECT * FROM students WHERE first_name LIKE %s OR last_name LIKE %s"
            search_term = f"%{search_value}%"
            results = self.db.fetch_query(query, (search_term, search_term))
        
        elif search_type == 'email':
            query = "SELECT * FROM students WHERE email = %s"
            results = self.db.fetch_query(query, (search_value,))
        
        else:
            print("Error: Invalid search type. Use 'id', 'name', or 'email'.")
            return None
        
        return results
    
    def get_all_students(self):
        """
        Get all students
        
        Returns:
            List of all students or None
        """
        query = "SELECT * FROM students ORDER BY student_id"
        return self.db.fetch_query(query)
    
    def _student_exists(self, student_id):
        """Check if student exists"""
        query = "SELECT student_id FROM students WHERE student_id = %s"
        return self.db.fetch_one(query, (student_id,)) is not None
    
    def display_student(self, student):
        """Display student information in formatted way"""
        print(f"\n{'='*60}")
        print(f"Student ID: {student[0]}")
        print(f"Name: {student[1]} {student[2]}")
        print(f"Gender: {student[3]}")
        print(f"Date of Birth: {student[4]}")
        print(f"Email: {student[5]}")
        print(f"Phone: {student[6]}")
        print(f"{'='*60}")
    
    def close_connection(self):
        """Close database connection"""
        self.db.close_connection()