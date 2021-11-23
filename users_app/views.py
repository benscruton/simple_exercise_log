from django.shortcuts import render, redirect
import bcrypt
from .models import User
from django.contrib import messages

# Create your views here.

def login_index(request):
    return render(request, "login_index.html")


def register_new_user(request):
    errors = User.objects.basic_validator(request.POST)

    if errors:
        for v in errors.values():
            messages.error(request, v)
        return redirect("/")

    this_user = User.objects.create(
        first_name = request.POST["first_name"],
        last_name = request.POST["last_name"],
        email = request.POST["email"],
        hashed_pw = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt()).decode()
        )

    request.session["user_id"] = this_user.id
    request.session["first_name"] = this_user.first_name
    request.session["last_name"] = this_user.last_name
    request.session["email"] = this_user.email
    request.session["last_act"] = "registered account"

    return redirect("/login/success")


def success(request):
    if not "user" in request.session:
        messages.error(request, "You must be logged in to view this page.")
        return redirect("/login")

    return render(request, "success.html")


def logout(request):
    del request.session["user"]
    request.session["last_act"] = "logged out"
    return redirect("/")


def login(request):
    try:
        this_user = User.objects.get(email = request.POST["email"])
    except:
        messages.error(request, "User not found!")
        return redirect("/login")

    match = bcrypt.checkpw(request.POST["password"].encode(), this_user.hashed_pw.encode())
    
    if not match:
        messages.error(request, "User and password didn't match.")
        return redirect("/login")

    request.session["user"] = {
        "id": this_user.id,
        "first_name": this_user.first_name,
        "last_name": this_user.last_name,
        "email": this_user.email
    }
    request.session["last_act"] = "logged in"
    
    return redirect("/")
