from django.db import models

# Create your models here.

class task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
class Contract(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name 

# class Author(models.Model):
#     author_name = models.CharField(default="author-1" ,max_length=100)
    
#     def __str__(self):
#         return self.author_name
      
    
class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    # author_name = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()
    language = models.CharField(max_length=30)
    
    def __str__(self):
        return self.title
    
    
class Teacher(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Student(models.Model):
    student_name = models.CharField(max_length=20)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=20)
    roll_number = models.CharField(max_length=20)
    validity_status = models.BooleanField(default=True) 
    
    def __str__(self):
        return self.student_name
    
class Section(models.Model):
    section_name = models.CharField(max_length=20)
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    
    def __str__(self):
        return self.section_name