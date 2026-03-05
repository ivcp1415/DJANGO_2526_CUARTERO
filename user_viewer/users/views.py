from django.shortcuts import render

# this method returns student data
def get_student(request):
    student_list = {
        'student1': {
            'id': 1,
            'name': 'Pau',
            'email': 'pau.serra@itic.cat',
            'rol': 'Delegat'
        },
        'student2': {
            'id': 2,
            'name': 'Laia',
            'email': 'laia.martinez@itic.cat',
            'rol': 'Subdelegada'
        },
        'student3': {
            'id': 3,
            'name': 'Marc',
            'email': 'marc.font@itic.cat',
            'rol': 'Estudiant'
        },
        'student4': {
            'id': 4,
            'name': 'Júlia',
            'email': 'julia.vila@itic.cat',
            'rol': 'Estudiant'
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
        }
    }
    context = {"msg": teacher_list}
    return render(request, '', context)