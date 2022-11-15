from django.contrib.postgres.fields import ArrayField
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)        

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)
    selected = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    difficulty_choices = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    time = models.PositiveSmallIntegerField()
    difficulty = models.CharField(max_length=200, choices=difficulty_choices)
    genre = models.ManyToManyField(Genre)
    ingredients = models.ManyToManyField(Ingredient)
    # ArrayField https://docs.djangoproject.com/en/4.1/ref/contrib/postgres/fields/
    # Querying ArrayField https://docs.djangoproject.com/en/2.0/ref/contrib/postgres/fields/#querying-arrayfield
    # Form https://docs.djangoproject.com/en/4.1/ref/contrib/postgres/forms/#simplearrayfield
    # steps = ArrayField(models.TextField(blank=True)) 
    favorited = models.BooleanField(default=False)
    planner = models.BooleanField(default=False)
    custom = models.BooleanField(default=False)
    step1 = models.TextField(default="", blank=False)
    step2 = models.TextField(default="", blank=True)
    step3 = models.TextField(default="", blank=True)
    step4 = models.TextField(default="", blank=True)
    step5 = models.TextField(default="", blank=True)
    step6 = models.TextField(default="", blank=True)
    step7 = models.TextField(default="", blank=True)
    step8 = models.TextField(default="", blank=True)
    step9 = models.TextField(default="", blank=True)
    step10 = models.TextField(default="", blank=True)
    step11 = models.TextField(default="", blank=True)
    step12 = models.TextField(default="", blank=True)
    step13 = models.TextField(default="", blank=True)
    step14 = models.TextField(default="", blank=True)
    step15 = models.TextField(default="", blank=True)
    step16 = models.TextField(default="", blank=True)
    step17 = models.TextField(default="", blank=True)
    step18 = models.TextField(default="", blank=True)
    step19 = models.TextField(default="", blank=True)
    step20 = models.TextField(default="", blank=True)


    def __str__(self):
        return self.name

class DiaryEntry(models.Model):
    #idk what to put here yet
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True)
