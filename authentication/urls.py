from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('student_profile/', views.student_profile, name='student_profile'),
    path('alumni_profile/', views.alumni_profile, name='alumni_profile')
]

