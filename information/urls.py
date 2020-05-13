from django.urls import path
from . import views

urlpatterns = {

    path('initpage/',views.initpage),
    path('initpage/initdetail/',views.initdetail),

    path('updatepage/',views.updatepage),
    path('updatepage/updatedetail/',views.updatedetail),

    path('querypage/',views.querypage),
    path('querypage/querydetail/',views.querydetail),

    path('recordpage/',views.recordpage),
    path('recordpage/recorddetail/',views.recordtdetail),

    path('medicalquerypage/',views.medicalquerypage),
    path('medicalquerypage/medicalquerydetail/',views.medicalquerydetail),

}

