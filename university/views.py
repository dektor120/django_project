from django.shortcuts import render, redirect
from .models import Student, Subject, Grade
from django.db.models import Avg
from django.http import Http404

def index(request):
    return render(request, 'university/index.html')

def students(request):
    students = Student.objects.all()
    return render(request, 'university/students.html', {'students': students})

def student_detail(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        raise Http404("Student does not exist")
    grades = Grade.objects.filter(student=student)
    context = {
        'student': student,
        'grades': grades,
    }
    return render(request, 'university/student_detail.html', context)

def subjects(request):
    subjects = Subject.objects.all()
    return render(request, 'university/subjects.html', {'subjects': subjects})

def subject_detail(request, subject_id):
    try:
        subject = Subject.objects.get(pk=subject_id)
    except Subject.DoesNotExist:
        raise Http404("Subject does not exist")
    grades = Grade.objects.filter(subject=subject)
    context = {
        'subject': subject,
        'grades': grades,
    }
    return render(request, 'university/subject_detail.html', context)

def grades(request):
    grades = Grade.objects.all()
    return render(request, 'university/grades.html', {'grades': grades})

def best_students(request):
    students_avg = Grade.objects.values('student__name').annotate(average_grade=Avg('grade')).order_by('-average_grade')[:3]
    return render(request, 'university/best_students.html', {'students_avg': students_avg})

def worst_students(request):
    students_avg = Grade.objects.values('student__name').annotate(average_grade=Avg('grade')).order_by('average_grade')[:3]
    return render(request, 'university/worst_students.html', {'students_avg': students_avg})

def subject_average(request):
    subjects_avg = Grade.objects.values('subject__name').annotate(average_grade=Avg('grade')).order_by('subject__name')
    return render(request, 'university/subject_average.html', {'subjects_avg': subjects_avg})