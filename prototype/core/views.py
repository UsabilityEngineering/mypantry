from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect("/")
                else:
                    return HttpResponse("Your account is not active.")
            else:
                return render(request, 'core/login.html', {"login_form": LoginForm})
    else:
        return render(request, 'core/login.html', {"login_form": LoginForm, "signed_out": True})

@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    return redirect("/")

@login_required(login_url='/login/')
def home(request):
    return render(request, 'core/home.html', {"login_form": LoginForm, "home_active": True})

@login_required(login_url='/login/')
def pantry(request):
    return render(request, 'core/pantry.html', {"pantry_active": True})

@login_required(login_url='/login/')
def browse_recipes(request):
    return render(request, 'core/browse_recipes.html', {"browse_recipes_active": True})

@login_required(login_url='/login/')
def saved_and_custom_recipes(request):
    return render(request, 'core/saved_and_custom_recipes.html', {"saved_and_custom_recipes_active": True})

@login_required(login_url='/login/')
def grocery_list(request):
    return render(request, 'core/grocery_list.html', {"grocery_list_active": True})

@login_required(login_url='/login/')
def food_diary(request):
    return render(request, 'core/food_diary.html', {"food_diary_active": True})

@login_required(login_url='/login/')
def reaction_reporter(request):
    return render(request, 'core/reaction_reporter.html', {"food_diary_active": True})