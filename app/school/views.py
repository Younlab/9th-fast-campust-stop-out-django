from django.shortcuts import render

from student.models import Student
from .models import School


def school_list(request):
    school = School.objects.all()
    context = {
        'schools': school
    }
    return render(request, 'school/school_list.html', context)


def school_detail(request, pk):
    school = School.objects.get(pk=pk)
    print(school)
    school_student = school.school_student.all()
    print(school_student)
    context = {
        'schools': school,
        'student': school_student,
    }
    return render(request, 'school/school_detail.html', context)
