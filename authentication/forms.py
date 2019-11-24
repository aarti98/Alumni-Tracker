from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, StudentDetail, AlumniDetail

PROFILE_CHOICES = [('student', 'Student'),
                    ('alumni', 'Alumni')]


class UserSignupForm(UserCreationForm):

    profile = forms.CharField(widget=forms.Select(choices=PROFILE_CHOICES))


    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model= CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'profile')


# class CustomUserChangeForm(UserChangeForm):

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email')


class StudentDetailForm(ModelForm):
    class Meta:
        model = StudentDetail
        exclude = ['user']

class AlumniDetailForm(ModelForm):
    class Meta:
        model = AlumniDetail
        exclude = ['user']
