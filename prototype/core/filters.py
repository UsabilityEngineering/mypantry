import django_filters

from .models import *

def filter_ingredients(queryset, name, value):
    if value:
        for recipe in queryset:
            for ingredient in recipe.ingredients.all():
                if not ingredient.selected:
                    queryset = queryset.exclude(id=recipe.id)
    return queryset

class RecipeFilter(django_filters.FilterSet):
    ingredient = django_filters.BooleanFilter(label="Filter by Ingredients", field_name="ingredients", method=filter_ingredients)
    name = django_filters.CharFilter(field_name="name", lookup_expr="icontains")
    class Meta:
        model = Recipe
        fields = ['name', 'difficulty', 'ingredient']