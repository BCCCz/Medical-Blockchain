from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login),
    path('login/detail/', views.detail),
]

