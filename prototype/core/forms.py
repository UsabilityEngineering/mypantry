import datetime
from django import forms
from django.forms import ModelForm
from django_select2 import forms as s2forms

from .models import *

class IngredientWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        "name__icontains"
    ]

class GenreWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        "name__icontains"
    ]

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
        widgets = {
            'ingredients': IngredientWidget,
            'genres': GenreWidget,
            'step1': forms.Textarea(attrs={'rows':4,'cols':15})
        }
    
    #Use Django Select2
    #https://django-select2.readthedocs.io/en/latest/

class DiaryEntryForm(ModelForm):
    date_cooked = forms.DateField(initial=datetime.date.today)

    class Meta:
        model = DiaryEntry
        fields = ('recipe_name', 'date_cooked', 'notes')

class ReactionEntryForm(ModelForm):
    date_experienced = forms.DateField(initial=datetime.date.today)

    class Meta:
        model = ReactionEntry
        fields = ('reactiontype', 'date_experienced', 'notes')
    