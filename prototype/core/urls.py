from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('pantry/', views.pantry, name='pantry'),
    path('browse_recipes/', views.browse_recipes, name='browse'),
    path('saved_and_custom_recipes/', views.saved_and_custom_recipes, name='saved'),
    path('grocery_list/', views.grocery_list, name='planner'),
    path('food_diary/', views.food_diary, name='diary'),
    path('reaction_reporter/', views.reaction_reporter, name='reporter'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('update_ingredient/<int:pk>', views.update_ingredient, name='update_ingredient'),
    path('update_selected', views.update_selected, name='update_selected'),
]