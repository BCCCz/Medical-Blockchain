from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage),
    path('page/',views.page),
]

