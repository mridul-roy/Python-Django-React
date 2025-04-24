from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import task, Contract, Books, Author
from .serializers import TaskSerializer, ContractSerializer, BooksSerializer, AuthorSerializer

# Create your views here.

class TaskViewSet(ModelViewSet):
    queryset = task.objects.all()
    serializer_class = TaskSerializer

class ContractViewSet(ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    
    
class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
class BooksViewSet(ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer