from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add-drug", views.addDrug, name="addDrug"),
    path("search-prescription", views.searchPrescription, name='searchPrescription')
]