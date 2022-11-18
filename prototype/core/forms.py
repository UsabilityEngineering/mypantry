import datetime
from django import forms
from django.forms import ModelForm
from django_select2 import forms as s2forms

from .models import *

class RecipeModelForm(ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'name', 'prep_time', 'cook_time', 'total_time', 
            'difficulty', 'genres', 'ingredients',
            'step1', 'step2', 'step3', 'step4', 'step5',
            'step6', 'step7', 'step8', 'step9', 'step10',
            'step11', 'step12', 'step13', 'step14', 'step15',
            'step16', 'step17', 'step18', 'step19', 'step20',
        ]
    
    #Use Django Select2
    #https://django-select2.readthedocs.io/en/latest/

    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

class DiaryEntryForm(ModelForm):
    date_cooked = forms.DateField(initial=datetime.date.today)

    class Meta:
        model = DiaryEntr
        fields = ('recipe_name', 'date_cooked', 'notes')
    