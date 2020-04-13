from django.urls import path
from . import views

urlpatterns = {
    path('initpage/',views.initpage),
    path('initpage/initdetail/',views.initdetail),


}

