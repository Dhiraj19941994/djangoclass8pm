from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
    path('add_student', views.add_student,name='add_student'),
    path('add_teacher', views.add_teacher,name='add_teacher'),
    path('', views.loginpage,name='loginpage'),
    path('dologin', views.dologin,name='dologin'),
    path('logout', views.logout_all,name='logout'),
    path('change_password', views.change_password,name='change_password'),
]
