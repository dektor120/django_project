from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Avg
from .models import Student, Subject, Grade
from .forms import StudentForm, SubjectForm, GradeForm



def index(request):
    return render(request, 'university/index.html')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'university/student_list.html', {'students': students})


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'university/student_form.html', {'form': form})


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'university/student_form.html', {'form': form})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'university/student_confirm_delete.html', {'student': student})


def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'university/subject_list.html', {'subjects': subjects})


def subject_create(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm()
    return render(request, 'university/subject_form.html', {'form': form})


def subject_update(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'university/subject_form.html', {'form': form})


def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject.delete()
        return redirect('subject_list')
    return render(request, 'university/subject_confirm_delete.html', {'subject': subject})


def grade_list(request):
    grades = Grade.objects.all()
    form = GradeFilterForm(request.GET)

    if form.is_valid():
        student = form.cleaned_data.get('student')
        subject = form.cleaned_data.get('subject')

        if student:
            grades = grades.filter(student=student)
        if subject:
            grades = grades.filter(subject=subject)

    order_by = request.GET.get('order_by', '')
    if order_by in ('student__name', '-student__name', 'subject__name', '-subject__name'):
        grades = grades.order_by(order_by)

    context = {
        'grades': grades,
        'form': form,
    }
    return render(request, 'university/grade_list.html', context)


def grade_create(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = GradeForm()
    return render(request, 'university/grade_form.html', {'form': form})


def grade_update(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = GradeForm(instance=grade)
    return render(request, 'university/grade_form.html', {'form': form})


def grade_delete(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == 'POST':
        grade.delete()
        return redirect('grade_list')
    return render(request, 'university/grade_confirm_delete.html', {'grade': grade})


def best_students(request):
    students_avg = Grade.objects.values('student__name').annotate(
        average_grade=Avg('grade')
    ).filter(average_grade__gt=3.5).order_by('-average_grade')
    return render(request, 'university/best_students.html', {'students_avg': students_avg})


def worst_students(request):
    students_avg = Grade.objects.values('student__name').annotate(
        average_grade=Avg('grade')
    ).filter(average_grade__lte=3.5).order_by('average_grade')
    return render(request, 'university/worst_students.html', {'students_avg': students_avg})

def subject_average(request):
    subjects_avg = Grade.objects.values('subject__name').annotate(
        average_grade=Avg('grade')).order_by('subject__name')
    return render(request, 'university/subject_average.html', {'subjects_avg': subjects_avg})