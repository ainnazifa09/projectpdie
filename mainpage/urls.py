# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('studentregistration/', views.studentregistration, name='studentregistration'),
    path('profilepage/', views.profilepage, name='profilepage'),
    path('studentsignin/', views.studentsignin, name='studentsignin'),  
    path('lecturersignin/', views.lecturersignin, name='lecturersignin'),
    path('studentdashboard/', views.studentdashboard, name='studentdashboard'),  
    path('lecturerdashboard/', views.lecturerdashboard, name='lecturerdashboard'),

]
