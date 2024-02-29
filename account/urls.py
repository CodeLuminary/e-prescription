from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("submit", views.login, name="login"),
    path("get-users", views.getUsers, name='getusers'),
    path("add-user", views.addUser, name='adduser')
]