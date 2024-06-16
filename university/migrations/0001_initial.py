# Generated by Django 5.0.6 on 2024-06-16 22:29

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('group_number', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Номер группы должен состоять из цифр, может содержать дефис и русскую заглавную букву (например, 123-А).', regex='^[0-9]+(-[0-9А-Я]?)?$')], verbose_name='Номер группы')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название предмета')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(verbose_name='Оценка')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.student', verbose_name='Студент')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.subject', verbose_name='Предмет')),
            ],
        ),
    ]
