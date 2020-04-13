from django.urls import path
from . import views

urlpatterns = {
    path('init/',views.accountinit),
    path('update/', views.accountupdate),
    path('query/',views.meidcalquery),
    path('record/',views.medicalrecord),
    path('medicalquery/',views.meidcalquery),

}

