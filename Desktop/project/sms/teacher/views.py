from django.shortcuts import render
from user.models import StudentProfile,CustomUser
from django.shortcuts import redirect
from teacher import forms
from teacher.forms import NoticeForm,FoundItemForm,TeacherPPForm
from teacher.models import Notice,StudentAttendence,FoundItem,results,TeacherPP,TeacherProfile
from student.models import ClaimItem

# Create your views here.
def teacher_home(request):
    context={
    'name':'Lokendra',
    'age':70
    }
    return render(request,'teacher/teacher_home.html',context=context)

def view_student(request):
    all_student =StudentProfile.objects.all().order_by('-id')
    context={
    'all_student':all_student,

    }
    return render(request,'teacher/view_student.html',context=context)

def view_student_detail(request,id):
    student_view_detail = StudentProfile.objects.get(id=id)
    context={
    'student_view_detail':student_view_detail
    }
    return render(request,'teacher/view_student_detail.html',context=context)

def delete_student_page(request):
    all_student =StudentProfile.objects.all().order_by('-id')
    context={
    'all_student':all_student,
    }
    return render(request,'teacher/delete_student.html',context=context)

def delete_student(request,id):
    delete_student = StudentProfile.objects.get(id=id)
    delete_student.delete()
    return redirect('view_student')

def add_notice(request):
    form = forms.NoticeForm()
    if request.method == 'POST':
        form = forms.NoticeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect('view_notice')
    context = {
    'form':form
    }
    return render(request,'teacher/add_notice.html',context=context)

def view_notice(request):
    all_notice = Notice.objects.all().order_by('-uploaded_at')
    context={
    'all_notice':all_notice
    }
    return render(request,'teacher/view_notice.html',context=context)

def edit_notice_page(request):
    all_notice =Notice.objects.all()
    context ={
    'all_notice':all_notice
    }
    return render(request,'teacher/edit_notice_page.html',context=context)



def edit_notice(request,id):
    notice = Notice.objects.get(id=id)
    form = forms.NoticeForm(instance=notice)
    if request.method == 'POST':
        form =forms.NoticeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_notice')
    context = {
    'notice':notice,
    'form':form
    }
    return render(request,'teacher/edit_notice.html',context=context)

from tablib import Dataset
from teacher.resources import StudentAttendenceResource

def simple_upload(request):
    if request.method == 'POST':
        person_resource = StudentAttendenceResource()
        dataset = Dataset()
        new_person = request.FILES['myfile']
        imported_data = dataset.load(new_person.read(),format='xls')
        result = person_resource.import_data(dataset,dry_run=True)

        if not result.has_errors():
            person_resource.import_data(dataset,dry_run=False)
    return render(request,'teacher/import.html')

def view_attendence_page(request):
    all_student = StudentProfile.objects.all().order_by('-id')
    context = {
    'all_student':all_student,
    }
    return render(request,'teacher/view_attendence_page.html',context=context)

def view_attendence_detail(request,id):
    student_view_detail = StudentProfile.objects.get(id=id)
    student_attendence_detail = StudentAttendence.objects.filter(admin=id)
    context={
    'student_view_detail':student_view_detail,
    'student_attendence_detail':student_attendence_detail
    }
    return render(request,'teacher/view_attendence_detail.html',context=context)

def view_found_item(request):
    all_found_item = FoundItem.objects.all().order_by('-id')
    context={
    'all_found_item':all_found_item,
    }
    return render(request,'teacher/view_found_item.html',context=context)

def add_found_item(request):
    form = forms.FoundItemForm()
    if request.method == 'POST':
        form = forms.FoundItemForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect('view_found_item')
    context ={
    'form':form
    }
    return render(request,'teacher/add_found_item.html',context=context)

def claimed_items(request):
    claimed_item = ClaimItem.objects.all()
    context={
    'claimed_item':claimed_item
    }
    return render(request,'teacher/claimed_item.html',context=context)

def result_page(request):
    all_student =StudentProfile.objects.all().order_by('-id')
    context={
    'all_student':all_student,
    }
    return render(request,'teacher/result_page.html',context=context)

def add_result_page(request):
    all_student =StudentProfile.objects.all().order_by('-id')
    context={
    'all_student':all_student,
    }
    return render(request,'teacher/add_result_page.html',context=context)

def add_result(request,id):
    student = StudentProfile.objects.get(id=id)
    form = forms.AddResultForm()
    if request.method == 'POST':
        form = forms.AddResultForm(request.POST)
        if form.is_valid():
            ci=form.save(commit=False)
            ci.admin = student
            ci.save()
            return redirect('result_page')
    context={
    'student':student,
    'form':form,
    }
    return render(request,'teacher/add_result.html',context=context)

def view_detail_result(request,id):
    result = results.objects.get(admin=id)
    context={
    'result':result
    }
    return render(request,'teacher/view_detail_result.html',context=context)



def profile_picture(request,teacher_id,id):
    pp = TeacherPP.objects.get(id=id)
    teacher_id =TeacherProfile.objects.get(id=teacher_id)
    form = forms.TeacherPPForm(instance=pp)
    if request.method == 'POST':
        form =forms.TeacherPPForm(request.POST,request.FILES,instance=pp)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={
    'form':form,
    'pp':pp
    }
    return render(request,'teacher/add_teacher_profile.html',context=context)
