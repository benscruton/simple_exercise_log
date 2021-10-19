from django.shortcuts import render, redirect, HttpResponse
from .models import *

import datetime

# Create your views here.
def index(request):
    return redirect("/test")

def ajax_testing(request):
    return render(request, "ajax_testing.html")

def add_user(request):
    return "hello"

def add_workout(request):
    context = {}
    if "workout_errors" in request.session:
        context["errors"] = request.session["workout_errors"]
        del request.session["workout_errors"]
        context["submission"] = request.session["workout_submitted_info"]
        del request.session["workout_submitted_info"]
    return render(request, "workouts.html", context)

def create_workout(request):
    errors = Workout.objects.basic_validator(request.POST)
    if errors:
        request.session["workout_errors"] = errors
        request.session["workout_submitted_info"] = request.POST
        return redirect("/workouts/new")
    
    w = Workout.objects.create(
        type_of_exercise = request.POST["type"],
        duration = request.POST["duration"],
        notes = request.POST["notes"],
        date = datetime.datetime.strptime(
            request.POST["date"],
            "%Y-%m-%d"
        )
    )
    return redirect(f"/workouts/{w.id}")

def view_workout(request, workout_id):
    w = Workout.objects.get(id=workout_id)
    context = {}
    context["workout_type"] = w.type_of_exercise
    context["workout_date"] = datetime.datetime.strftime(w.date, "%b %d, %Y")
    duration = f"{w.duration // 60 + ' hours ' if w.duration >= 60 else ''}"
    duration += f"{w.duration % 60} minutes"
    context["workout_duration"] = duration
    context["workout_notes"] = w.notes
    return render(request, "workout_detail.html", context)