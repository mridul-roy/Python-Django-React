from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('pr/admin/', views.admin, name='admin'),
    path('editor/', views.editor, name='editor'),
    path('author/', views.author, name='author'),

]