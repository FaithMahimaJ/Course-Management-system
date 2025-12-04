from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Student,courses
from .forms import studentForm,CourseForm,RegisterForm
from django.contrib.auth.decorators import login_required




# def home(request):
#     return HttpResponse("Welcome to the students home page")
# def about(request):
#     return HttpResponse("This is the about page for students")
# def contact(request):
#     return HttpResponse("<h1>Contact page</h1><p>phone:123-456-7890</p>")
# def home(request):
#     return render(request,"home.html")
# def about(request):
#     return render(request,"about.html")
# def contact(request):
#     return render(request,"contact.html")

def home(request):
    context={
        "title":"Welcome Uma!",
        "msg":"This is dynamic content from Django."
    }
    return render(request,"home.html",context)

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request, "contact.html")

# def list_student(request):
#     data = Student.objects.all()
#     return render(request,"list_student.html",{"student":data})

def courses_list(request):
    data=courses.objects.all()
    return render(request,"list_course.html",{"course":data})

#list students

def student_list(request):
    student = Student.objects.all()
    return render(request,"student_list.html",{"student": student})


# from django.shortcuts import render,HttpResponse
# from .forms import MyForm

# def home(request):
#     form = MyForm()
#     if request.method == "POST":
#         form = MyForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#     return render(request, "homee.html",{"form":form})

#add students 

def add_student(request):
    if request.method== "POST":
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/student/')
    else:
        form = studentForm()
    return render(request,"add_student.html",{"form": form})

#edit student 

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method=="POST":
        form = studentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/student/')
    else:
        form = studentForm(instance=student)
    return render(request, "edit_student.html", {"form": form})
        
#delete student 

def delete_student(request, id):
    student = get_object_or_404 (Student, id=id)
    student.delete()
    return redirect('/student/')

def add_course(request):
    if request.method=='POST':
        form=CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/courses/')
    else:
        form=CourseForm()
    return render(request,'add_course.html',{'form':form})

def edit_course(request,id):
    course_obj=get_object_or_404(courses,id=id)
    if request.method=='POST':
        form=CourseForm(request.POST,instance=course_obj)
        if form.is_valid():
            form.save()
            return redirect('/courses/')
    else:
        form=CourseForm(instance=course_obj)
    return render(request,'edit_course.html',{'form':form})

def delete_course(request,id):
    course_obj=get_object_or_404(courses,id=id)
    course_obj.delete()
    return redirect('/courses/')
def view_status(request):
    value=courses.objects.filter(status=True)
    return render(request,'status.html',{'course':value})



from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate

def register_user(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form=RegisterForm()
    return render(request,'register.html',{'form':form})

#Login functrionality

def login_user(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('/dashboard/')
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})   

#Logout functionality

def logout_user(request):
    logout(request)
    return redirect('/login/')

#project pages(login required)

from django.contrib.auth.decorators import login_required
@login_required(login_url='/login/')
def dashboard(request):
    return render(request,'dashboard.html')

