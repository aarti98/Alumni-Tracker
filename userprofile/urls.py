from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.display_post, name='post_list'),
]