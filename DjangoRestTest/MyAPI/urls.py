from django.urls import path
from .views import pais,index

urlpatterns = [
    path('pais/',pais),
    path('',index),
]