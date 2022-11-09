from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

#Reference this model using get_user_model() or settings.AUTH_USER_MODEL
#https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#referencing-the-user-model

class Category(models.Model):
    name = models.CharField(max_length=200)        

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)

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
    steps = models.JSONField()

    def __str__(self):
        return self.name

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    pantry = models.ManyToManyField(Ingredient)
    planner = models.ManyToManyField(Recipe)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class DiaryEntry(models.Model):
    #idk what to put here yet
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
