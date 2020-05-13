from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('prevention/',views.prevention),
    path('faqs/',views.faqs),
]

