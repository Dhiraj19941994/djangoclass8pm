from django.shortcuts import render
from teacher.models import FoundItem,results
from user.models import StudentProfile
from student import forms
from django.shortcuts import redirect

# Create your views here.
def student_home(request):
    context={
    'name':'Mausma',
    'age':20
    }
    return render(request,'student/student_home.html',context=context)

def view_found_item_student(request):
    admin_id =request.user
    all_found_item = FoundItem.objects.all().order_by('-id')
    context={
    'all_found_item':all_found_item,
    'admin_id':admin_id
    }
    return render(request,'student/view_found_item_student.html',context=context)

def claim_item(request,admin_id,id):
    all_found_item = FoundItem.objects.get(id=id)
    user = StudentProfile.objects.get(admin=admin_id)
    form =forms.ClaimItemForm()
    if request.method == 'POST':
        form = forms.ClaimItemForm(request.POST)
        if form.is_valid():
            ci = form.save(commit=False)
            ci.admin1 =user
            ci.admin =all_found_item
            ci.save()
            return redirect('view_found_item_student')
    context ={
    'form':form,
    }
    return render(request,'student/claim_found_item.html',context=context)

def view_result_student(request,id):
    result = results.objects.get(admin=id)
    context={
    'result':result
    }
    return render(request,'student/view_result_student.html',context=context)
