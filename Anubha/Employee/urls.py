from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('authenticate', views.authenticate, name = 'authenticate'),
    path('leave', views.leave, name = 'leave'),
]