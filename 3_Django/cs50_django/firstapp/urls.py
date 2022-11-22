from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("viet", views.viet, name="viet"),
    path("truc", views.truc, name="truc"),
    path("<str:name>", views.greet, name="greet")
]