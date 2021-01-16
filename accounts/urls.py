from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from accounts.viewsets import CustomUserModelViewSet
from . import  views

router=DefaultRouter()
router.register('users',CustomUserModelViewSet)
urlpatterns = [
    path('data/', views.UserRetrieveUpdateDestroyAPIView.as_view(),
         name='user-data'),  # get data for the currently logged in user
    path("", include(router.urls)),  # provides a few default

]
