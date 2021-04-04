from django.contrib import admin
from django.urls import path
from teacher import views

urlpatterns = [
    path('teacher_home', views.teacher_home,name='teacher_home'),
    path('view_student', views.view_student,name='view_student'),
    path('view_student_detail/<id>', views.view_student_detail,name='view_student_detail'),
    path('delete_student_page', views.delete_student_page,name='delete_student_page'),
    path('delete_student/<id>', views.delete_student,name='delete_student'),
    path('add_notice', views.add_notice,name='add_notice'),
    path('view_notice', views.view_notice,name='view_notice'),
    path('edit_notice_page', views.edit_notice_page,name='edit_notice_page'),
    path('edit_notice/<id>', views.edit_notice,name='edit_notice'),
    path('simple_upload', views.simple_upload,name='simple_upload'),
    path('view_attendence_page', views.view_attendence_page,name='view_attendence_page'),
    path('view_attendence_detail/<id>', views.view_attendence_detail,name='view_attendence_detail'),
    path('view_found_item', views.view_found_item,name='view_found_item'),
    path('add_found_item', views.add_found_item,name='add_found_item'),
    path('claimed_items', views.claimed_items,name='claimed_items'),
    path('result_page', views.result_page,name='result_page'),
    path('add_result_page', views.add_result_page,name='add_result_page'),
    path('add_result/<id>', views.add_result,name='add_result'),
    path('view_detail_result/<id>', views.view_detail_result,name='view_detail_result'),
    path('profile_picture/<teacher_id>/<id>', views.profile_picture,name='profile_picture'),

]
