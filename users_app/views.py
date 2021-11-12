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
        for k, v in errors.items():
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
    if not "user_id" in request.session:
        messages.error(request, "You must be logged in to view this page.")
        return redirect("/login")

    return render(request, "success.html")


def logout(request):
    del request.session["user_id"]
    del request.session["first_name"]
    del request.session["last_name"]
    del request.session["email"]
    del request.session["last_act"]
    return redirect("/login")


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

    request.session["user_id"] = this_user.id
    request.session["first_name"] = this_user.first_name
    request.session["last_name"] = this_user.last_name
    request.session["email"] = this_user.email
    request.session["last_act"] = "logged in"
    
    return redirect("/login/success")
