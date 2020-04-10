from django.urls import path
from . import views

urlpatterns = [
    path('information/', views.user_inforation),
]

