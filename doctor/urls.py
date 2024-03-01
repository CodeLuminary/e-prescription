from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("addpatient", views.addpatient, name="addpatient"),
    path("prescribe-drug", views.prescribeDrug, name="prescribedrug")
]