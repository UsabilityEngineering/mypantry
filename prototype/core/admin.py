from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *

#admin.site.register(Model)
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Genre)
admin.site.register(Recipe)