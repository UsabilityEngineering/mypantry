# Generated by Django 4.0.2 on 2022-11-10 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_selected_recipe_favorited_recipe_planner'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='custom',
            field=models.BooleanField(default=False),
        ),
    ]
