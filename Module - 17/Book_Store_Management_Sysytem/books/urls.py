from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('add_book/', views.add_book, name='add_book'),
    path('update_book/<int:id>/', views.update_book, name='update_book'),
    path('delete_book/<int:id>/', views.delete_book, name='delete_book'),

]