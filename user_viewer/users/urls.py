from django.urls import path
from . import views

urlpatterns = [
    path('get_students/', views.get_students),
    path('get_teachers/', views.get_teachers)
]