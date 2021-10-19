from django.shortcuts import render, redirect, HttpResponse
from .models import *

# Create your views here.
def index(request):
    return redirect("/test")

def ajax_testing(request):
    return render(request, "ajax_testing.html")

def add_user(request):
    return "hello"

def add_workout(request):
    return render(request, "new_workout.html")

def create_workout(request):
    errors = Workout.objects.basic_validator(request.POST)
    if errors:
        return HttpResponse("That isn't going to work")
    printer = "*"*50 + "\n\n"
    printer += f"type:     {request.POST['type']}\n"
    printer += f"duration: {request.POST['duration']}\n"
    printer += f"notes:    {request.POST['notes']}\n"
    printer += "\n" + "*"*50
    print(printer)
    return redirect("/workouts/new")