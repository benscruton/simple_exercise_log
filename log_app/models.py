from django.db import models

# Create your models here.

class Workout(models.Model):
    type_of_exercise = models.CharField(max_length=255)
    duration = models.IntegerField()
    date = models.DateField()
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)