from django.shortcuts import render

from .models import Student


def student_list(request):
    student = Student.objects.all()
    context = {
        'students': student,
    }
    return render(request, 'student/student_list.html', context)


def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    student_friend = student.friend.all()
    context = {
        'students': student,
        'student_friend': student_friend,
    }
    return render(request, 'student/student_detail.html', context)
