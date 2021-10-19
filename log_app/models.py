from django.db import models

import datetime

# Create your models here.

class WorkoutManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}

        if not len(post_data["type"]):
            errors["type"] = "Workout type is required."

        try:
            workout_length = int(post_data["duration"])
            duration_is_valid = (workout_length > 0)
        except:
            duration_is_valid = False
        if not duration_is_valid:
            errors["duration"] = "Duration must be a number greater than 0."

        try:
            datetime.datetime.strptime(post_data["date"], "%Y-%m-%d")
            date_is_valid = True
        except:
            date_is_valid = False
        if not date_is_valid:
            errors["date"] = "Please enter a valid date (format: YYYY-MM-DD)"

        return errors

class Workout(models.Model):
    type_of_exercise = models.CharField(max_length=255)
    duration = models.IntegerField()
    date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = WorkoutManager()