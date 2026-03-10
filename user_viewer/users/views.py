from django.shortcuts import render
from .models import Student, Teacher

def get_students(request):
    # get all students
    all_students = Student.objects.all()
    response = {"Students": all_students}
    return render(request, "students.html", response)

def get_teachers(request):
    # get all teachers
    all_teachers = Teacher.objects.all()
    print(f"DEBUG: Found {all_teachers.count()} teachers in DB")  # <--- ADD THIS
    response = {"Teachers": all_teachers}
    return render(request, "teachers.html", response)

# get specific student
def get_student_by_id(request, pk):
    # get by id
    student_obj = Student.objects.get(id=pk)
    context = {'student': student_obj}
    return render(request, 'student_page.html', context)

#get specific teacher
def get_teacher_by_id(request, pk):
    teacher_obj = Teacher.objects.get(id=pk)
    context = {"teacher": teacher_obj}
    return render(request, 'teacher_page.html', context)