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

# this method returns student data
def get_student(request):
    student_list = {
        'student1': {
            'id': 1,
            'name': 'Pau',
            'email': 'pau.serra@itic.cat',
            'rol': 'Delegat',
            'mean': 9.2
        },
        'student2': {
            'id': 2,
            'name': 'Laia',
            'email': 'laia.martinez@itic.cat',
            'rol': 'Subdelegada',
            'mean': '9.4'
        },
        'student3': {
            'id': 3,
            'name': 'Marc',
            'email': 'marc.font@itic.cat',
            'rol': 'Estudiant',
            'mean': '9.5'
        },
        'student4': {
            'id': 4,
            'name': 'Júlia',
            'email': 'julia.vila@itic.cat',
            'rol': 'Estudiant',
            'mean': 9.0
        }
    }
    context = {'msg': student_list}
    return render(request, 'students.html', context)

def get_teacher(request):
    teacher_list = {
        'teacher1': {
            'id': 101,
            'name': 'Marta',
            'email': 'marta.rodriguez@itic.cat',
            'department': 'Matemàtiques',
            'is_tutor': True
        },
        'teacher2': {
            'id': 102,
            'name': 'Albert',
            'email': 'albert.ferrer@itic.cat',
            'department': 'Informàtica',
            'is_tutor': False
        },
        'teacher3': {
            'id': 103,
            'name': 'Sílvia',
            'email': 'silvia.puig@itic.cat',
            'department': 'Física',
            'is_tutor': True
        },
        'teacher4': {
            'id': 104,
            'name': 'Marta',
            'email': 'marta.tarrells@itic.cat',
            'department': 'Llengua Catalana',
            'is_tutor': False
        }
    }
    context = {"msg": teacher_list}
    return render(request, 'teachers.html', context)