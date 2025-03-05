from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .forms import BookForm



# Create your views here.
def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def add_book(request):
    if request.method == 'POST':
        forms = BookForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    else:
        forms = BookForm()
        return render(request, 'add_book.html', {'forms': forms})


def update_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        forms = BookForm(request.POST, request.FILES, instance=book)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    else:
        forms = BookForm(instance=book)
        return render(request, 'update_book.html', {'forms': forms})
    
def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('home')
