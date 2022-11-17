# Generated by Django 4.0.2 on 2022-11-10 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_customuser_pantry_customuser_planner_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diaryentry',
            name='user',
        ),
        migrations.AddField(
            model_name='diaryentry',
            name='recipe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.recipe'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='selected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recipe',
            name='selected',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]