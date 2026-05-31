# Student Management System

A comprehensive Python-based Student Management System using MySQL database. This project provides a complete solution for managing students, courses, and enrollments with an interactive command-line interface.

## Features

### Student Management
- ✅ Add new students
- ✅ Update student information
- ✅ Delete students
- ✅ Search students by ID, name, or email
- ✅ View all students

### Course Management
- ✅ Add new courses
- ✅ Update course information
- ✅ Delete courses
- ✅ Search courses by ID or name
- ✅ View all courses

### Enrollment Management
- ✅ Enroll students in courses
- ✅ Remove enrollments
- ✅ View student's courses
- ✅ View students in a course
- ✅ Update grades
- ✅ View all enrollments

### Reports
- ✅ System summary (total students, courses, enrollments)
- ✅ Detailed enrollment summary
- ✅ Students per course
- ✅ Courses per student
- ✅ Course popularity analysis
- ✅ Student performance summary

## Project Structure

```
GIT_DBMS_PTOJECT_322/
│
├── database/
│   ├── schema.sql          # Database schema creation
│   └── sample_data.sql     # Sample data for testing
│
├── src/
│   ├── db_connection.py    # Database connection management
│   ├── student.py          # Student management module
│   ├── course.py           # Course management module
│   ├── enrollment.py       # Enrollment management module
│   ├── reports.py          # Reports generation module
│   └── main.py             # Main application entry point
│
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore file
└── README.md               # This file
```

## Software Requirements

- **Python**: 3.11 or higher
- **MySQL**: 5.7 or higher
- **pip**: Python package manager

## Installation Steps

### 1. Clone or Download the Project

```bash
git clone https://github.com/smanasviyadav-ship-it/GIT_DBMS_PTOJECT_322.git
cd GIT_DBMS_PTOJECT_322
```

### 2. Create Python Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Setup MySQL Database

#### Option A: Using Command Line

```bash
# Connect to MySQL
mysql -u root -p

# In MySQL prompt, run the schema file
source database/schema.sql
source database/sample_data.sql
```

#### Option B: Using MySQL Workbench or GUI

1. Open MySQL Workbench or your preferred MySQL client
2. Create a new connection with your credentials
3. Open `database/schema.sql` and execute it
4. Open `database/sample_data.sql` and execute it

### 5. Configure Environment Variables

1. Copy `.env.example` to `.env`:

```bash
# On Windows
copy .env.example .env

# On macOS/Linux
cp .env.example .env
```

2. Edit `.env` and update with your MySQL credentials:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=student_management_system
```

## Running the Application

### Start the Application

```bash
# Make sure virtual environment is activated
python src/main.py
```

### Application Menu

Once launched, you'll see the main menu with options:

```
============================================================
               STUDENT MANAGEMENT SYSTEM
============================================================

1.  Student Management
2.  Course Management
3.  Enrollment Management
4.  View Reports
5.  Exit
```

## Usage Examples

### Adding a Student

1. Select option `1` from main menu (Student Management)
2. Select option `1` (Add Student)
3. Enter student details:
   - First Name: John
   - Last Name: Doe
   - Gender: Male
   - Date of Birth: 2003-05-15
   - Email: john.doe@university.edu
   - Phone: 555-0101

### Enrolling a Student in a Course

1. Select option `3` from main menu (Enrollment Management)
2. Select option `1` (Enroll Student in Course)
3. Enter:
   - Student ID: 1
   - Course ID: 1
   - Enrollment Date: (leave blank for today)

### Viewing Reports

1. Select option `4` from main menu (View Reports)
2. Choose from available reports:
   - System Summary
   - Enrollment Summary
   - Students Per Course
   - Courses Per Student
   - Course Popularity
   - Student Performance Summary

## Database Schema

### Students Table
```sql
- student_id (INT, PRIMARY KEY, AUTO_INCREMENT)
- first_name (VARCHAR 50)
- last_name (VARCHAR 50)
- gender (VARCHAR 10)
- date_of_birth (DATE)
- email (VARCHAR 100, UNIQUE)
- phone (VARCHAR 20)
- created_at (TIMESTAMP)
- updated_at (TIMESTAMP)
```

### Courses Table
```sql
- course_id (INT, PRIMARY KEY, AUTO_INCREMENT)
- course_name (VARCHAR 100)
- credits (INT)
- description (TEXT)
- created_at (TIMESTAMP)
- updated_at (TIMESTAMP)
```

### Enrollments Table
```sql
- enrollment_id (INT, PRIMARY KEY, AUTO_INCREMENT)
- student_id (INT, FOREIGN KEY)
- course_id (INT, FOREIGN KEY)
- enrollment_date (DATE)
- grade (VARCHAR 2)
- created_at (TIMESTAMP)
- updated_at (TIMESTAMP)
```

## Features Highlights

### Security
- ✅ Parameterized SQL queries (prevents SQL injection)
- ✅ Input validation for all user inputs
- ✅ Environment-based configuration

### Code Quality
- ✅ Object-Oriented Programming (OOP) principles
- ✅ Comprehensive error handling
- ✅ Detailed comments and docstrings
- ✅ Modular architecture

### User Experience
- ✅ Interactive menu-driven interface
- ✅ Clear error messages
- ✅ Formatted output
- ✅ Input validation with feedback

## Troubleshooting

### Connection Error: "Can't connect to MySQL server"

**Solution:**
1. Ensure MySQL service is running
2. Check your `.env` file credentials
3. Verify MySQL is listening on the configured port
4. Check firewall settings

### Import Error: "No module named 'mysql'"

**Solution:**
```bash
# Ensure virtual environment is activated, then:
pip install mysql-connector-python
```

### Database Error: "Unknown database 'student_management_system'"

**Solution:**
1. Run the schema.sql file to create the database
2. Verify you're connected to the correct MySQL server
3. Check your DB_NAME in .env file

## Sample Data

The `sample_data.sql` file includes:
- 8 sample students
- 8 sample courses
- 16 sample enrollments with grades

This allows you to test all features immediately after setup.

## Performance Considerations

- Database indexes created on frequently queried columns
- Foreign key constraints maintain data integrity
- Unique constraints prevent duplicate entries
- Timestamps for audit trail

## Future Enhancements

Possible improvements for future versions:
- Web-based GUI using Flask/Django
- User authentication and authorization
- Advanced reporting with data export (PDF, Excel)
- Batch import/export functionality
- Email notifications for enrollment
- GPA calculation for students
- Prerequisite course management

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open-source and available under the MIT License.

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review the code comments
3. Ensure all requirements are met
4. Verify database connectivity

## Author

Created as a comprehensive Student Management System demonstration.

---

**Last Updated**: 2024
**Version**: 1.0.0