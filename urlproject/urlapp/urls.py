from django.urls import path
from . import views


urlpatterns = [
    path("", views.home),
    path("add_url/", views.add_url, name="add_url"),
    path("stats/<str:url>", views.url, name="dynamic_url"),
    path("delete/<str:url>", views.delete, name="delete_url")
]