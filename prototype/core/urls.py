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
    path('update_selected', views.update_selected_ingredients, name='update_selected'),
    path('update_planner/<int:pk>', views.update_planner, name='update_planner'),
    path('update_planner_content_recipes', views.update_planner_content_recipes, name='update_planner_recipes'),
    path('update_planner_content_ingredients', views.update_planner_content_ingredients, name='update_planner_ingredients'),
    path('update_diary/<int:pk>', views.update_diary, name='update_diary'),
    path('update_favorite/<int:pk>', views.update_favorite, name='update_favorite'),
    path('update_favorite_content', views.update_favorite_content, name='update_favorite_content'),
    path('update_diary_content', views.update_diary_content, name='update_diary_content'),
]