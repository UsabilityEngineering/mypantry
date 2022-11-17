from django.shortcuts import render, redirect
from django.http import HttpResponse
import uuid, json

from .forms import *
from .models import *

def home(request):
    return render(request, 'core/home.html', {"home_active": True})

def pantry(request):
    ingredients = Ingredient.objects.all()
    categories = Category.objects.all().order_by('name').exclude(name="Default")

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
    planner = Recipe.objects.all().filter(planner=True)
    missing = []
    for recipe in planner:
        for ingredient in recipe.ingredients:
            if ingredient.selected == false:
                missing.append(ingredient)

    context = {
        'planner': planner,
        'missing': missing,

        "grocery_list_active": True,
    }
    return render(request, 'core/grocery_list.html', context)

def food_diary(request):
    return render(request, 'core/food_diary.html', {"food_diary_active": True})

def reaction_reporter(request):
    return render(request, 'core/reaction_reporter.html', {"food_diary_active": True})

def create_recipe(request):
    form = RecipeModelForm()

    if request.method == 'POST':
        form = RecipeModelForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.uuid = uuid.uuid4()
            recipe.author = "MyPantry"
            #recipe.custom = True
            recipe.save()
            for genre in form.cleaned_data.get('genres'):
                recipe.genres.add(genre)
            for ingredient in form.cleaned_data.get('ingredients'):
                recipe.ingredients.add(ingredient)
            return redirect('saved')
    
    context = {
        'form': form,
    }
    return render(request, 'core/recipe_form.html', context)

#Updating model using AJAX
#https://stackoverflow.com/questions/46322894/change-a-django-model-with-javascript

def update_ingredient(request, pk):
    ingredient = Ingredient.objects.get(id=pk)
    ingredient.selected = ingredient.selected^True
    ingredient.save()
    response_data={'val':ingredient.selected^True}
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def update_selected(request):
    selected = Ingredient.objects.all().filter(selected=True).order_by('name')

    context = {
        'selected': selected,
    }
    return render(request, 'core/selected_ingredients.html', context)
