from django.contrib import admin
from teacher.models import StudentAttendence

# Register your models here.


from import_export.admin import ImportExportModelAdmin

class StudentAttendenceAdmin(ImportExportModelAdmin):
    list_dispaly =('admin','date','class1','class2','class3','class4','class5',)
admin.site.register(StudentAttendence,ImportExportModelAdmin)
