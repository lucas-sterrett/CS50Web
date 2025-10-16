from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lucas", views.lucas, name="lucas"),
    path("<str:name>", views.greet, name="greet")
]