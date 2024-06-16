from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name= ("ФИО"))
    group_number = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^[0-9]+(-[0-9А-Я]?)?$',
                message='Номер группы должен состоять из цифр, '
                        'может содержать дефис и русскую заглавную букву (например, 123-А).'
            ),
        ],
        verbose_name= ("Номер группы")
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Студент")
        verbose_name_plural = ("Студенты")

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name= ("Название предмета"))

    def clean(self):
        super().clean()
        if Subject.objects.filter(name__iexact=self.name).exists():
            raise ValidationError({'name': 'Предмет с таким названием уже существует.'})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Предмет")
        verbose_name_plural = ("Предметы")

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name= ("Студент"))
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name= ("Предмет"))
    grade = models.IntegerField(verbose_name= ("Оценка"))

    def __str__(self):
        return f"{self.student} - {self.subject}: {self.grade}"

