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
    class Meta:
        model = Grade
        fields = ['student', 'subject', 'grade']


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