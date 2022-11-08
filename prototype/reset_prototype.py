import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MyPantryPrototype.settings")
django.setup()
from django.contrib.auth.models import User

demo_user = User.objects.create_user('demo1', password='chico')
demo_user2 = User.objects.create_user('demo2', password='chico')
demo_user.save()
demo_user2.save()