from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import StudentInfo,StudentAcademics

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']

class StudentinfoForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = "__all__"