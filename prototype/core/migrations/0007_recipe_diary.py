# Generated by Django 4.0.2 on 2022-11-29 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_diaryentr_diaryentry_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='diary',
            field=models.BooleanField(default=False),
        ),
    ]