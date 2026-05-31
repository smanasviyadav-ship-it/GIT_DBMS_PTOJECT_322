"""
Course Management Module
Handles course CRUD operations
"""

from db_connection import DatabaseConnection

class Course:
    """Manages course operations"""
    
    def __init__(self):
        """Initialize course manager with database connection"""
        self.db = DatabaseConnection()
    
    def add_course(self, course_name, credits, description=""):
        """
        Add a new course
        
        Args:
            course_name: Name of the course
            credits: Number of credits
            description: Course description
            
        Returns:
            Boolean indicating success/failure
        """
        # Input validation
        if not course_name:
            print("Error: Course name is required.")
            return False
        
        if not isinstance(credits, int) or credits <= 0:
            print("Error: Credits must be a positive integer.")
            return False
        
        # Check if course already exists
        query = "SELECT course_id FROM courses WHERE course_name = %s"
        if self.db.fetch_one(query, (course_name,)):
            print(f"Error: Course '{course_name}' already exists.")
            return False
        
        # Insert course
        query = """INSERT INTO courses (course_name, credits, description) 
                   VALUES (%s, %s, %s)"""
        
        if self.db.execute_query(query, (course_name, credits, description)):
            print(f"✓ Course '{course_name}' added successfully.")
            return True
        else:
            print("Error: Failed to add course.")
            return False
    
    def update_course(self, course_id, course_name=None, credits=None, description=None):
        """
        Update course information
        
        Args:
            course_id: Course ID to update
            Other args: Fields to update (None means no change)
            
        Returns:
            Boolean indicating success/failure
        """
        # Check if course exists
        if not self._course_exists(course_id):
            print(f"Error: Course with ID {course_id} not found.")
            return False
        
        # Build update query dynamically
        updates = []
        params = []
        
        if course_name:
            updates.append("course_name = %s")
            params.append(course_name)
        
        if credits is not None:
            if not isinstance(credits, int) or credits <= 0:
                print("Error: Credits must be a positive integer.")
                return False
            updates.append("credits = %s")
            params.append(credits)
        
        if description is not None:
            updates.append("description = %s")
            params.append(description)
        
        if not updates:
            print("Error: No fields to update.")
            return False
        
        params.append(course_id)
        query = f"UPDATE courses SET {', '.join(updates)} WHERE course_id = %s"
        
        if self.db.execute_query(query, params):
            print(f"✓ Course ID {course_id} updated successfully.")
            return True
        else:
            print("Error: Failed to update course.")
            return False
    
    def delete_course(self, course_id):
        """
        Delete a course
        
        Args:
            course_id: Course ID to delete
            
        Returns:
            Boolean indicating success/failure
        """
        if not self._course_exists(course_id):
            print(f"Error: Course with ID {course_id} not found.")
            return False
        
        query = "DELETE FROM courses WHERE course_id = %s"
        
        if self.db.execute_query(query, (course_id,)):
            print(f"✓ Course ID {course_id} deleted successfully.")
            return True
        else:
            print("Error: Failed to delete course.")
            return False
    
    def search_course(self, search_type, search_value):
        """
        Search for courses
        
        Args:
            search_type: 'id' or 'name'
            search_value: Value to search for
            
        Returns:
            List of matching courses or None
        """
        if search_type == 'id':
            query = "SELECT * FROM courses WHERE course_id = %s"
            results = self.db.fetch_query(query, (search_value,))
        
        elif search_type == 'name':
            query = "SELECT * FROM courses WHERE course_name LIKE %s"
            search_term = f"%{search_value}%"
            results = self.db.fetch_query(query, (search_term,))
        
        else:
            print("Error: Invalid search type. Use 'id' or 'name'.")
            return None
        
        return results
    
    def get_all_courses(self):
        """
        Get all courses
        
        Returns:
            List of all courses or None
        """
        query = "SELECT * FROM courses ORDER BY course_id"
        return self.db.fetch_query(query)
    
    def _course_exists(self, course_id):
        """Check if course exists"""
        query = "SELECT course_id FROM courses WHERE course_id = %s"
        return self.db.fetch_one(query, (course_id,)) is not None
    
    def display_course(self, course):
        """Display course information in formatted way"""
        print(f"\n{'='*60}")
        print(f"Course ID: {course[0]}")
        print(f"Course Name: {course[1]}")
        print(f"Credits: {course[2]}")
        print(f"Description: {course[3] if len(course) > 3 else 'N/A'}")
        print(f"{'='*60}")
    
    def close_connection(self):
        """Close database connection"""
        self.db.close_connection()