from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    return render(request, 'core/home.html', {"home_active": True})

def pantry(request):
    return render(request, 'core/pantry.html', {"pantry_active": True})

def browse_recipes(request):
    return render(request, 'core/browse_recipes.html', {"browse_recipes_active": True})

def saved_and_custom_recipes(request):
    return render(request, 'core/saved_and_custom_recipes.html', {"saved_and_custom_recipes_active": True})

def grocery_list(request):
    return render(request, 'core/grocery_list.html', {"grocery_list_active": True})

def food_diary(request):
    return render(request, 'core/food_diary.html', {"food_diary_active": True})

def reaction_reporter(request):
    return render(request, 'core/reaction_reporter.html', {"food_diary_active": True})