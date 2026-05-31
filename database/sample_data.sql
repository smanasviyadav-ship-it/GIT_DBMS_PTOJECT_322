-- Sample Data for Student Management System

USE student_management_system;

-- Insert sample students
INSERT INTO students (first_name, last_name, gender, date_of_birth, email, phone) VALUES
('John', 'Doe', 'Male', '2003-05-15', 'john.doe@university.edu', '555-0101'),
('Jane', 'Smith', 'Female', '2003-08-22', 'jane.smith@university.edu', '555-0102'),
('Michael', 'Johnson', 'Male', '2002-12-10', 'michael.johnson@university.edu', '555-0103'),
('Sarah', 'Williams', 'Female', '2004-03-18', 'sarah.williams@university.edu', '555-0104'),
('David', 'Brown', 'Male', '2003-07-25', 'david.brown@university.edu', '555-0105'),
('Emily', 'Davis', 'Female', '2002-11-30', 'emily.davis@university.edu', '555-0106'),
('Robert', 'Miller', 'Male', '2003-09-12', 'robert.miller@university.edu', '555-0107'),
('Lisa', 'Wilson', 'Female', '2004-01-05', 'lisa.wilson@university.edu', '555-0108');

-- Insert sample courses
INSERT INTO courses (course_name, credits, description) VALUES
('Python Programming', 3, 'Introduction to Python programming language'),
('Database Management', 4, 'SQL and database design fundamentals'),
('Web Development', 3, 'HTML, CSS, and JavaScript for web development'),
('Data Science', 4, 'Introduction to data analysis and machine learning'),
('Software Engineering', 3, 'Software development methodologies and practices'),
('Cloud Computing', 3, 'AWS, Azure, and cloud infrastructure'),
('Mobile Development', 3, 'Android and iOS application development'),
('Artificial Intelligence', 4, 'Machine learning and AI algorithms');

-- Insert sample enrollments
INSERT INTO enrollments (student_id, course_id, enrollment_date, grade) VALUES
(1, 1, '2024-01-15', 'A'),
(1, 2, '2024-01-15', 'B+'),
(2, 1, '2024-01-15', 'A-'),
(2, 3, '2024-01-15', 'A'),
(3, 2, '2024-01-15', 'B'),
(3, 4, '2024-01-15', 'A'),
(4, 1, '2024-01-15', 'B+'),
(4, 5, '2024-01-15', 'A'),
(5, 3, '2024-01-15', 'B'),
(5, 6, '2024-01-15', 'B+'),
(6, 2, '2024-01-15', 'A'),
(6, 7, '2024-01-15', 'A-'),
(7, 4, '2024-01-15', 'B+'),
(7, 8, '2024-01-15', 'A'),
(8, 1, '2024-01-15', 'A'),
(8, 5, '2024-01-15', 'B');