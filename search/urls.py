from django.urls import path
from .views import SearchResultView

urlpatterns = [
    path('users/', SearchResultView.as_view(), name='result')
]