"""
Database Connection Module
Handles MySQL database connections and basic operations
"""

import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class DatabaseConnection:
    """Manages database connection and operations"""
    
    def __init__(self):
        """Initialize database connection"""
        try:
            self.connection = mysql.connector.connect(
                host=os.getenv('DB_HOST', 'localhost'),
                user=os.getenv('DB_USER', 'root'),
                password=os.getenv('DB_PASSWORD', ''),
                database=os.getenv('DB_NAME', 'student_management_system'),
                port=int(os.getenv('DB_PORT', 3306))
            )
            
            if self.connection.is_connected():
                db_info = self.connection.get_server_info()
                print(f"Successfully connected to MySQL Server version {db_info}")
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            self.connection = None
    
    def get_connection(self):
        """Return the database connection object"""
        return self.connection
    
    def is_connected(self):
        """Check if connection is active"""
        if self.connection is None:
            return False
        return self.connection.is_connected()
    
    def execute_query(self, query, params=None):
        """
        Execute a query (INSERT, UPDATE, DELETE)
        
        Args:
            query: SQL query string with %s placeholders
            params: Tuple of parameters for the query
            
        Returns:
            Boolean indicating success/failure
        """
        try:
            if not self.is_connected():
                print("Database connection lost!")
                return False
            
            cursor = self.connection.cursor()
            
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            self.connection.commit()
            cursor.close()
            return True
        
        except Error as e:
            print(f"Error executing query: {e}")
            self.connection.rollback()
            return False
    
    def fetch_query(self, query, params=None):
        """
        Execute a SELECT query
        
        Args:
            query: SQL query string with %s placeholders
            params: Tuple of parameters for the query
            
        Returns:
            List of tuples containing query results
        """
        try:
            if not self.is_connected():
                print("Database connection lost!")
                return None
            
            cursor = self.connection.cursor()
            
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            results = cursor.fetchall()
            cursor.close()
            return results
        
        except Error as e:
            print(f"Error fetching query: {e}")
            return None
    
    def fetch_one(self, query, params=None):
        """
        Execute a SELECT query and return single result
        
        Args:
            query: SQL query string with %s placeholders
            params: Tuple of parameters for the query
            
        Returns:
            Single tuple or None
        """
        try:
            if not self.is_connected():
                print("Database connection lost!")
                return None
            
            cursor = self.connection.cursor()
            
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            result = cursor.fetchone()
            cursor.close()
            return result
        
        except Error as e:
            print(f"Error fetching single result: {e}")
            return None
    
    def close_connection(self):
        """Close the database connection"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed.")