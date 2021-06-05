from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("home", views.index , name="home"),
    path("books", views.books , name="books"),
    path("facilities", views.facilities, name="facilities"),
    path("about", views.about, name="about"),
    path("read1", views.read1, name="read1")
]