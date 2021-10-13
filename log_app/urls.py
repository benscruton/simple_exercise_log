from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("test", views.ajax_testing),
    path("users/new", views.add_user),
]
