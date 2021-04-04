from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here0.
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

class CustomUser(AbstractUser):
    user_type_data = ((1,'teacher'),(2,'student'))
    user_type = models.CharField(choices=user_type_data,max_length=20)

class StudentProfile(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='student_profile')
    faculty = models.CharField(choices=FACULTY,max_length=20)
    year = models.CharField(choices=YEAR,max_length=20)
    semester = models.CharField(choices=SEMESTER,max_length=20)
    address = models.CharField(max_length=200)
    bio = models.CharField(max_length=500)
    objects = models.Manager()

    def __str__(self):
        return self.admin.username

class TeacherProfile(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='teacher_profile')
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.admin.username

@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            TeacherProfile.objects.create(admin=instance,address='')
        if instance.user_type==2:
            StudentProfile.objects.create(admin=instance,address='',faculty='',semester='',bio='',year='')

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.teacher_profile.save()
    if instance.user_type==2:
        instance.student_profile.save()
