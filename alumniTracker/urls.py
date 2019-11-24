
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='homepage'),
    path('authentication/', include('authentication.urls')),
    path('home/', include('post.urls')),
    path('search/', include('search.urls')),
    path('userprofile/', include('userprofile.urls'))
]
