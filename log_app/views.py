from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return redirect("/test")

def ajax_testing(request):
    return render(request, "ajax_testing.html")

def add_user(request):
    return "hello"