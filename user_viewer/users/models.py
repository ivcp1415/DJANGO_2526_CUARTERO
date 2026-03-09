from django.db import models

# Create your models here.
# student model
class Student(models.Model):
    f_name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    rol = models.CharField(max_length=30)
    mean = models.DecimalField(max_digits=4, decimal_places=2)

# teacher model
class Teacher(models.Model):
    f_name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    department = models.CharField(max_length=30)
    is_tutor = models.BooleanField()


