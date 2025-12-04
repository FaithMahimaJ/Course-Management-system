from django.urls import path
from .views import home, about, contact,student_list,courses_list,add_student,edit_student,delete_student
from  .views import add_course, edit_course, delete_course,register_user,login_user,logout_user,dashboard,view_status
urlpatterns=[
    path('home/', home),
    path('about/', about),
    path('contact/', contact),
    path('student/', student_list,name='student_list'),
    path('courses/',courses_list,name='courses_list'),

    path('student/add/',add_student,name='add_student'),
    path('student/edit/<int:id>/',edit_student,name='edit_student'),
    path('student/delete/<int:id>/',delete_student,name='delete_student'),
    path('courses/add/',add_course,name='add_course'),
    path('courses/edit/<int:id>/',edit_course,name='edit_course'),
    path('courses/delete/<int:id>/',delete_course,name='delete_course'),
    path('course/status/', view_status, name='view_status'),

    path('register/',register_user,name='register_user'),
    path('login/',login_user,name='login_user'),
    path('logout/',logout_user,name='logout_user'),
    path('dashboard/',dashboard,name='dashboard'),

]

# from django.contrib import admin
# from django.urls import path

# from student import views
# urlpatterns=[
#     path('home/',views.home,name='home')
# ]