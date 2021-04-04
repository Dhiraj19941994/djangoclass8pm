from django.contrib import admin
from django.urls import path
from student import views

urlpatterns = [
    path('student_home', views.student_home,name='student_home'),
    path('view_found_item_student', views.view_found_item_student,name='view_found_item_student'),
    path('claim_item/<admin_id>/<id>', views.claim_item,name='claim_item'),
    path('view_result_student/<id>', views.view_result_student,name='view_result_student'),
]
