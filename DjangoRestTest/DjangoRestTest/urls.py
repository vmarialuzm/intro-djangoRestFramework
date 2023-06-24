from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('MyAPI/',include('MyAPI.urls')),
    path('todos/',include('todos.urls')),
]
