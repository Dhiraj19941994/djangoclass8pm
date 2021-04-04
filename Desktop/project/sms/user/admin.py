from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import CustomUser,StudentProfile,TeacherProfile

# Register your models here.
class CustomUserAdmin(UserAdmin):
    pass
    # model = CustomUser
    # fieldsets = UserAdmin.fieldsets + (
    # (None,{'fields':('user_type',)}),)

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(StudentProfile)
admin.site.register(TeacherProfile)
