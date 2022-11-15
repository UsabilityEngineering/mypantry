from django import forms
from django.forms import ModelForm

from .models import Recipe

class RecipeModelForm(ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'name', 'time', 'difficulty', 'genre', 'ingredients',
            'step1', 'step2', 'step3', 'step4', 'step5',
            'step6', 'step7', 'step8', 'step9', 'step10',
            'step11', 'step12', 'step13', 'step14', 'step15',
            'step16', 'step17', 'step18', 'step19', 'step20',
        ]
        widgets = {
            'genre': forms.CheckboxSelectMultiple,
            'ingredients': forms.CheckboxSelectMultiple,
        }
    