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
    return render(request, "new_workout.html", context)

def create_workout(request):
    errors = Workout.objects.basic_validator(request.POST)
    if errors:
        request.session["workout_errors"] = errors
        request.session["workout_submitted_info"] = request.POST
        return redirect("/workouts/new")

    printer = f"type:     {request.POST['type']}<br/>"
    printer += f"duration: {request.POST['duration']}<br/>"
    printer += f"notes:    {request.POST['notes']}<br/>"
    date = request.POST["date"]
    print(type(date))
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    date = datetime.date(year = date.year, month = date.month, day = date.day)
    printer += f"date: <blockquote>{datetime.datetime.strftime(date, 'year: %Y<br/>month: %B<br/>day: %d')}</blockquote>"
    return HttpResponse(printer)