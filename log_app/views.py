from django.shortcuts import render, redirect
from .models import *

import datetime

# Create your views here:
def index(request):
    return redirect("/workouts")

def ajax_testing(request):
    return render(request, "ajax_testing.html")

def add_user(request):
    return "hello"

def create_workout_return_row(request):
    errors = Workout.objects.basic_validator(request.POST)
    if errors:
        return None
    w = Workout.objects.create(
        type_of_exercise = request.POST["type"],
        duration = request.POST["duration"],
        notes = request.POST["notes"],
        date = datetime.datetime.strptime(
            request.POST["date"],
            "%Y-%m-%d"
        )
    )
    w.duration = number_to_hours_minutes(int(w.duration))
    w.date = datetime.datetime.strftime(
        w.date, "%b %d, %Y"
    )
    print(type(w.date))
    context = {
        "w": w
    }
    return render(request, "_new_workout_row.html", context)


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
    context["workout_duration"] = number_to_hours_minutes(w.duration)
    context["workout_notes"] = w.notes
    return render(request, "workout_detail.html", context)

def all_workouts(request):
    all_workouts = list(Workout.objects.all())
    for w in all_workouts:
        w.duration = number_to_hours_minutes(w.duration)
    all_workouts.sort(key = lambda w: w.date, reverse=True)
    context = {
        "workouts": all_workouts
    }
    return render(request, "index.html", context)

def delete_workout(request, workout_id):
    w = Workout.objects.get(id=workout_id)
    w.delete()
    return redirect("/workouts")


def number_to_hours_minutes(duration):
    output = f"{f'{duration // 60} hour' if duration >= 60 else ''}"
    output += "s " if duration >= 120 else " "
    output += f"{duration % 60} minutes"
    return output.strip()