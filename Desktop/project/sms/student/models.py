from django.db import models
from teacher.models import FoundItem
from user.models import StudentProfile

# Create your models here.

class ClaimItem(models.Model):
    admin1=models.ForeignKey(StudentProfile,on_delete=models.CASCADE)
    admin=models.ForeignKey(FoundItem,on_delete=models.CASCADE)
    claim = models.BooleanField()
