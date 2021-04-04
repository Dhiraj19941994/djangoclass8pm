from django import forms
from user.models import CustomUser,StudentProfile,TeacherProfile

FACULTY = (
    ('1','BCA'),
    ('2','IT'),
    ('3','BE'),
    ('4','BSCCSIT'),
)
YEAR =(
('1','First'),
('2','Second'),
('3','Third'),
('4','Fourth'),
)

SEMESTER =(
    ('1','I'),
    ('2','II'),
)

class AddStudentForm(forms.Form):
    email = forms.EmailField(label='Email',max_length=80,widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password',max_length=80,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label='First Name',max_length=80,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Last Name',max_length=80,widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(label='Username',max_length=80,widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(label='Address',max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
    bio = forms.CharField(label='Bio',max_length=80,widget=forms.TextInput(attrs={'class':'form-control'}))
    semester = forms.ChoiceField(choices=SEMESTER)
    year = forms.ChoiceField(choices=YEAR)
    faculty = forms.ChoiceField(choices=FACULTY)

class AddTeacherForm(forms.Form):
    email = forms.EmailField(label='Email',max_length=80,widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password',max_length=80,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label='First Name',max_length=80,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Last Name',max_length=80,widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(label='Username',max_length=80,widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(label='Address',max_length=200,widget=forms.TextInput(attrs={'class':'form-control'}))
