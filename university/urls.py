from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('students/', views.student_list, name='student_list'),
     path('students/create/', views.student_create, name='student_create'),
     path('students/<int:pk>/update/', views.student_update, name='student_update'),
     path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
     path('subjects/', views.subject_list, name='subject_list'),
     path('subjects/create/', views.subject_create, name='subject_create'),
     path('subjects/<int:pk>/update/', views.subject_update, name='subject_update'),
     path('subjects/<int:pk>/delete/', views.subject_delete, name='subject_delete'),
     path('grades/', views.grade_list, name='grade_list'),
     path('grades/create/', views.grade_create, name='grade_create'),
     path('grades/<int:pk>/update/', views.grade_update, name='grade_update'),
     path('grades/<int:pk>/delete/', views.grade_delete, name='grade_delete'),
     path('best_students/', views.best_students, name='best_students'),
     path('worst_students/', views.worst_students, name='worst_students'),
     path('subject_average/', views.subject_average, name='subject_average'),
]