from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Faculty, ProjectStaff, Staff


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateFacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'
        exclude = ['user']


class UpdateProjectStaffForm(forms.ModelForm):
    class Meta:
        model = ProjectStaff
        fields = '__all__'
        exclude = ['user']


class UpdateStaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'
        exclude = ['user']
