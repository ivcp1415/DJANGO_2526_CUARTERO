from django.urls import path
from . import views

urlpatterns = [
    path('get_students/', views.get_students, name='students'),
    path('get_teachers/', views.get_teachers, name='teachers'),
    path('student/<int:pk>/', views.get_student_by_id, name='student'),
    path('teacher/<int:pk>/', views.get_teacher_by_id, name='teacher')
]