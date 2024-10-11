from django.db import models
from datetime import date

# Task 1: Author and Book Models with ForeignKey Relationship
class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Author Name")
    
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ['name']  # Orders authors alphabetically by name
    
    def __str__(self):
        return self.name
    
    def book_count(self):
        return self.book_set.count()  # Return the number of books associated with this author


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Author")  # Moved to the top
    title = models.CharField(max_length=200, verbose_name="Book Title")

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ['title']  # Orders books alphabetically by title

    def __str__(self):
        return self.title


# Task 2: Student and Course Models with ManyToManyField
class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="Course Name")

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ['name']  # Orders courses alphabetically by name

    def __str__(self):
        return self.name


class Student(models.Model):
    courses = models.ManyToManyField(Course, verbose_name="Courses Enrolled")  # Moved to the top
    name = models.CharField(max_length=100, verbose_name="Student Name")
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Date of Birth")  # For Task 3

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ['name']  # Orders students alphabetically by name

    def __str__(self):
        return self.name

    # Method to list all courses
    def list_courses(self):
        return ", ".join([course.name for course in self.courses.all()])

    # Task 3: Property to calculate age
    @property
    def age(self):
        if self.date_of_birth:
            today = date.today()
            return today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
            )
        return None
