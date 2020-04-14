from django.urls import path
from . import views

urlpatterns = {
    path('initpage/',views.initpage),
    path('initpage/initdetail/',views.initdetail),
    path('querypage/',views.querypage),
    path('querypage/querydetail/',views.accountquery),
}

