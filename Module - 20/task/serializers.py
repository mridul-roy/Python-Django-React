from rest_framework import serializers
from .models import task,Contract,Books, Author


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = '__all__'  
        
        
class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        
        
class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'