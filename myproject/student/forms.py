from django import forms
from .models import Student,courses

# class MyForm(forms.Form):
#     name = forms.CharField()
#     age = forms.IntegerField()
#     email = forms.EmailField()
#     city = forms.CharField()

# from django import forms
# from .models import Student,courses

class studentForm(forms.ModelForm):
    class Meta:
        model=Student 
        fields=['name','age','email','city']

class CourseForm(forms.ModelForm):
    class Meta:
        model=courses
        fields=['title','duration','fees','trainer_name','description','status']


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email']