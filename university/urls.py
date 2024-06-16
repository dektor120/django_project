from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('students/', views.students, name='students'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    path('subjects/', views.subjects, name='subjects'),
    path('subjects/<int:subject_id>/', views.subject_detail, name='subject_detail'),
    path('grades/', views.grades, name='grades'),
    path('best_students/', views.best_students, name='best_students'),
    path('worst_students/', views.worst_students, name='worst_students'),
    path('subject_average/', views.subject_average, name='subject_average'),
]