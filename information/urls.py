from django.urls import path
from . import views

urlpatterns = {
    path('initpage/',views.initpage),
    path('initdetail/',views.initdetail),

    path('updatepage/', views.updatepage),
    path('updatedetail/', views.updatedetail)

    path('querypage/', views.queryepage),
    path('querydetail/', views.querydetail)

    path('queryepage/', views.querypage),
    path('recorddetail/', views.querydetail)

    path('medicalquerypage/', views.medicalquerypage),
    path('medicalquerydetail/', views.medicalquerydetail)
}

