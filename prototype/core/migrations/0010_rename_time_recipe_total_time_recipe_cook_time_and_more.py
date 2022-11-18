# Generated by Django 4.0.2 on 2022-11-16 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_recipe_steps_recipe_step1_recipe_step10_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='time',
            new_name='total_time',
        ),
        migrations.AddField(
            model_name='recipe',
            name='cook_time',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='prep_time',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
