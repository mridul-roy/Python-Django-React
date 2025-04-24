from django.urls import path,include
from .views import TaskViewSet, ContractViewSet, BooksViewSet, AuthorViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('task', TaskViewSet, basename='task')
router.register('contract', ContractViewSet, basename='contract')
router.register('books', BooksViewSet, basename='books')
router.register('author', AuthorViewSet, basename='author')

urlpatterns = [
    path('', include(router.urls)),
]