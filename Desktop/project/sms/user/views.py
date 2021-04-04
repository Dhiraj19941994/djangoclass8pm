from django.shortcuts import render,redirect
from user import forms
from user.forms import AddStudentForm,AddTeacherForm
from user.models import CustomUser,StudentProfile,TeacherProfile
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.

def add_student(request):
    form = AddStudentForm()
    if request.method =='POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            address = form.cleaned_data['address']
            faculty = form.cleaned_data['faculty']
            year = form.cleaned_data['year']
            semester = form.cleaned_data['semester']
            bio = form.cleaned_data['bio']
            user = CustomUser.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name,user_type=2)
            user.student_profile.address =address
            user.student_profile.faculty =faculty
            user.student_profile.year =year
            user.student_profile.semester =semester
            user.student_profile.bio =bio
            user.save()
            messages.success(request,'You are added successfully as a student. Now You can log in')
            return HttpResponseRedirect(reverse('loginpage'))
    return render(request,'user/add_student.html',{'form':form})

def add_teacher(request):
    form = AddTeacherForm()
    if request.method =='POST':
        form = AddTeacherForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            address = form.cleaned_data['address']
            user = CustomUser.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name,user_type=1)
            user.teacher_profile.address =address
            user.save()
            messages.success(request,'You are added successfully as a teacher. Now You can log in')
            return HttpResponseRedirect(reverse('loginpage'))
    return render(request,'user/add_teacher.html',{'form':form})

def loginpage(request):
    if request.user.is_authenticated:
        print('all okay')
        user_type = request.user.user_type
        print(user_type)
        if user_type == '1':
            return redirect('teacher_home')
        elif user_type == '2':
            return redirect('student_home')
    return render(request,'user/login.html')

def dologin(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    user = authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        user_type = user.user_type
        if user_type == '1':
            return redirect('teacher_home')
        elif user_type == '2':
            return redirect('student_home')
        else:
            messages.error(request,'Login failed. Please try again')
            return('login')
    else:
        messages.error(request,'Invalid username or Password')
        return render(request,'user/login.html')
    return render(request,'user/login.html')

def logout_all(request):
    logout(request)
    return HttpResponseRedirect('/')

def change_password(request):
    user = request.user
    form = PasswordChangeForm(user)
    if request.method == 'POST':
        form = PasswordChangeForm(user=user,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('loginpage'))
    context={'form':form}
    return render(request,'user/change_password.html',context=context)
