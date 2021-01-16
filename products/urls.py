from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from accounts.viewsets import CustomUserModelViewSet
from products.views import ProductViewSet, CategoryViewSet
from . import  views

router=DefaultRouter()
router.register("",ProductViewSet)
router.register("/category",CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),  # provides a few default
]
