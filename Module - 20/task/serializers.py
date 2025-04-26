from rest_framework import serializers
from .models import task,Contract,Books, Teacher, Student, Section


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = '__all__'  
        
        
class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = '__all__'
        
        
class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
        
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'    
