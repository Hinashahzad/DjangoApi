from django.contrib import admin
from django.urls import path, include
from api.views import *
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path("", include(router.urls))
]
