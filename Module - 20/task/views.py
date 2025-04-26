from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import task, Contract, Books, Teacher, Student, Section
from .serializers import TaskSerializer, ContractSerializer, BooksSerializer, TeacherSerializer, StudentSerializer, SectionSerializer

# Create your views here.

class TaskViewSet(ModelViewSet):
    queryset = task.objects.all()
    serializer_class = TaskSerializer

class ContractViewSet(ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    
# class AuthorViewSet(ModelViewSet):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer  
    
class BooksViewSet(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    
class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class SectionViewSet(ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer