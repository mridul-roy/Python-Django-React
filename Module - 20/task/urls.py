from django.urls import path,include
from .views import TaskViewSet, ContractViewSet, BooksViewSet, TeacherViewSet, StudentViewSet, SectionViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('task', TaskViewSet, basename='task')
router.register('contract', ContractViewSet, basename='contract')
router.register('books', BooksViewSet, basename='books')
router.register('teacher', TeacherViewSet, basename='teacher')
router.register('student', StudentViewSet, basename='student')
router.register('section', SectionViewSet, basename='section')  

urlpatterns = [
    path('', include(router.urls)),
]