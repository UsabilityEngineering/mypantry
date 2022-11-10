from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *

def home(request):
    return render(request, 'core/home.html', {"home_active": True})

def pantry(request):
    ingredients = Ingredient.objects.all()
    categories = Category.objects.all()

    selected = ingredients.filter(selected=True)

    context = {
        'ingredients': ingredients,
        'categories': categories,
        'selected': selected,

        "pantry_active": True,
    }
    return render(request, 'core/pantry.html', context)

def browse_recipes(request):
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,

        "browse_recipes_active": True,
    }
    return render(request, 'core/browse_recipes.html', context)

def recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)

    context = {
        'recipe': recipe,
    }
    return render(request, 'core/recipe.html', context)

def saved_and_custom_recipes(request):
    recipes = Recipe.objects.all()
    
    saved = recipes.filter(favorited=True)
    custom = recipes.filter(custom=True)

    context = {
        'saved': saved,
        'custom': custom,

        "saved_and_custom_recipes_active": True,
    }
    return render(request, 'core/saved_and_custom_recipes.html', context)

def grocery_list(request):
    return render(request, 'core/grocery_list.html', {"grocery_list_active": True})

def food_diary(request):
    return render(request, 'core/food_diary.html', {"food_diary_active": True})

def reaction_reporter(request):
    return render(request, 'core/reaction_reporter.html', {"food_diary_active": True})