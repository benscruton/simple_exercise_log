from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("test", views.ajax_testing),
    path("users/new", views.add_user),
    path("workouts", views.all_workouts),
    path("workouts/create", views.create_workout),
    path("workouts/<int:workout_id>/delete", views.delete_workout),
    path("workouts/create/return_row", views.create_workout_return_row),
    path("workouts/<int:workout_id>", views.view_workout),
]
