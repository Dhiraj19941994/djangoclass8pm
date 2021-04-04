from django.db import models
from user.models import StudentProfile
from django.db.models.signals import post_save,pre_save,post_delete,pre_delete
from user.models import TeacherProfile
from django.dispatch import receiver


# Create your models here.

class Notice(models.Model):
    notice_subject = models.TextField()
    notice_image = models.ImageField(upload_to='notice')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class StudentAttendence(models.Model):
    admin = models.ForeignKey(StudentProfile,on_delete=models.CASCADE)
    clss1 =models.CharField(max_length=50)
    clss2 =models.CharField(max_length=50)
    clss3 =models.CharField(max_length=50)
    clss4 =models.CharField(max_length=50)
    clss5 =models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.admin.admin.username

class FoundItem(models.Model):
    found_item_name = models.CharField(max_length=80)
    found_item_detail = models.TextField()
    found_item_image = models.ImageField(max_length=80)

class results(models.Model):
    admin = models.ForeignKey(StudentProfile,on_delete=models.CASCADE)
    microprocessor =models.IntegerField()
    digital_logic =models.IntegerField()
    maths =models.IntegerField()
    english =models.IntegerField()
    database =models.IntegerField()
    coa =models.IntegerField()

# class Detail(models.Model):
#     detail = models.CharField(max_length=300)
#
# def post_detail(sender,instance,**kwargs):
#     print('Yes signals is working. we have new data on our database.')
#
# def pre_detail(sender,instance,**kwargs):
#     print('Something has been done before save method has been called.')
#
# def post_detail_delete(sender,instance,**kwargs):
#     print('Post delete signal')
#
# def pre_detail_delete(sender,instance,**kwargs):
#     print('Pre delete signal')
#
# post_save.connect(post_detail,sender=Detail)
# pre_save.connect(pre_detail,sender=Detail)
# post_delete.connect(post_detail_delete,sender=Detail)
# pre_delete.connect(pre_detail_delete,sender=Detail)

class TeacherPP(models.Model):
    admin = models.OneToOneField(TeacherProfile,on_delete=models.CASCADE,related_name='teacher_profile_picture')
    pp = models.ImageField()


@receiver(post_save,sender=TeacherProfile)
def teacherpp(sender,instance,created,**kwargs):
    if created:
        TeacherPP.objects.create(admin=instance)
