from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserSignupForm
from .models import CustomUser, AlumniDetail, StudentDetail


# class CustomUserAdmin(UserAdmin):
#     add_form = UserSignupForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username']

admin.site.register(CustomUser, UserAdmin)
admin.site.register(AlumniDetail)
admin.site.register(StudentDetail)
