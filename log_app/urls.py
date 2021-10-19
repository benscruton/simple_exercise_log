from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("test", views.ajax_testing),
    path("users/new", views.add_user),
    path("workouts/new", views.add_workout),
    path("workouts/create", views.create_workout),
    path("workouts/<int:workout_id>", views.view_workout),
]
