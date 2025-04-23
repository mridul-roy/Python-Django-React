from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .decotators import admin_required, editor_required, author_required

# Create your views here.

def home(request):
    return render(request, 'home.html')

@admin_required
def admin(request):
    return render(request, 'admin.html')

@editor_required
def editor(request):
    return render(request, 'editor.html')

@author_required
def author(request):
    return render(request, 'author.html')