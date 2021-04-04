from import_export import resources
from .models import StudentAttendence

class StudentAttendenceResource(resources.ModelResource):
    class Meta:
        model = StudentAttendence
