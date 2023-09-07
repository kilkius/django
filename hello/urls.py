from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ignas/", views.ignas, name="ignas"),
    path("<str:name>", views.greet, name="greet")
]