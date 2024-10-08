# Django Model Relationships Project

This is a Django project demonstrating model relationships, methods, properties, and admin integration. The project includes models for `Author`, `Book`, `Student`, and `Course` with `ForeignKey` and `ManyToManyField` relationships.

## Features
1. **Author and Book Models**: 
   - Authors can have multiple books.
   - A method in `Author` returns the number of books.
   
2. **Student and Course Models**: 
   - Students can enroll in multiple courses.
   - A method in `Student` lists all enrolled courses.

3. **Student Age Property**: 
   - Calculates a student's age based on their `date_of_birth` field.

