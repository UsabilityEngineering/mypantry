import datetime
from django import forms
from django.forms import ModelForm
from django_select2 import forms as s2forms

from .models import *

class IngredientWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = [
        "name__icontains",
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
            'name': forms.TextInput(attrs={'placeholder':"Recipe Name"}),
            'ingredients': IngredientWidget,
            'genres': GenreWidget,
            'step1': forms.Textarea(attrs={'rows':3,'cols':89}),
            'step2': forms.Textarea(attrs={'rows':3,'cols':89}),
            'step3': forms.Textarea(attrs={'rows':3,'cols':89}),
            'step4': forms.Textarea(attrs={'rows':3,'cols':89}),
            'step5': forms.Textarea(attrs={'rows':3,'cols':89}),
            'step6': forms.Textarea(attrs={'rows':3,'cols':89}),
            'step7': forms.Textarea(attrs={'rows':3,'cols':89}),
            'step8': forms.Textarea(attrs={'rows':3,'cols':89}),
            'step9': forms.Textarea(attrs={'rows':3,'cols':89}),
            'step10': forms.Textarea(attrs={'rows':3,'cols':89}),
            'step11': forms.Textarea(attrs={'rows':3,'cols':89}),
            'step12': forms.Textarea(attrs={'rows':3,'cols':89}),
            'step13': forms.Textarea(attrs={'rows':3,'cols':89}),
            'step14': forms.Textarea(attrs={'rows':3,'cols':89}),
            'step15': forms.Textarea(attrs={'rows':3,'cols':89}),
            'step16': forms.Textarea(attrs={'rows':3,'cols':89}),
            'step17': forms.Textarea(attrs={'rows':3,'cols':89}),
            'step18': forms.Textarea(attrs={'rows':3,'cols':89}),
            'step19': forms.Textarea(attrs={'rows':3,'cols':89}),
            'step20': forms.Textarea(attrs={'rows':3,'cols':89}),
        }
    
    #Use Django Select2
    #https://django-select2.readthedocs.io/en/latest/

class DiaryEntryForm(ModelForm):
    date_cooked = forms.DateField(initial=datetime.date.today)

    class Meta:
        model = DiaryEntry
        fields = ('recipe_name', 'date_cooked', 'notes')
        widgets = {
            'notes': forms.Textarea(attrs={'rows':8,'cols':25})
        }

class ReactionEntryForm(ModelForm):
    date_experienced = forms.DateField(initial=datetime.date.today)

    class Meta:
        model = ReactionEntry
        fields = ('reactiontype', 'date_experienced', 'notes')
    