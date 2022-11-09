# Generated by Django 4.0.2 on 2022-11-09 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_category_genre_ingredient_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='pantry',
            field=models.ManyToManyField(to='core.Ingredient'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='planner',
            field=models.ManyToManyField(to='core.Recipe'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='author',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='DiaryEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
