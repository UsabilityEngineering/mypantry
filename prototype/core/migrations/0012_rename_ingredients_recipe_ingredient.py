# Generated by Django 4.0.2 on 2022-11-16 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_recipe_name_concat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='ingredients',
            new_name='ingredient',
        ),
    ]
