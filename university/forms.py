from django import forms
from .models import Student, Subject, Grade

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'group_number']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']

class GradeForm(forms.ModelForm):
    GRADE_CHOICES = [(i, i) for i in range(1, 6)]
    grade = forms.ChoiceField(
        choices=GRADE_CHOICES,
        label='Оценка'
    )

    class Meta:
        model = Grade
        fields = ['student', 'subject', 'grade']
        labels = {
            'student': ('Студент'),
            'subject': ('Предмет'),
        }

class GradeFilterForm(forms.Form):
    student = forms.ModelChoiceField(
        queryset=Student.objects.all(),
        label='Студент',
        required=False,
        empty_label="Все студенты"
    )
    subject = forms.ModelChoiceField(
        queryset=Subject.objects.all(),
        label='Предмет',
        required=False,
        empty_label="Все предметы"
    )