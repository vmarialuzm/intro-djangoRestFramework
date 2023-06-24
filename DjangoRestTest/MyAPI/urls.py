from django.urls import path
from .views import pais,index

from rest_framework import routers
from .api import UserViewSet

router = routers.DefaultRouter()

router.register('api/users',UserViewSet,'users')

urlpatterns = router.urls

""" urlpatterns = [
    path('pais/',pais),
    path('',index),
] """