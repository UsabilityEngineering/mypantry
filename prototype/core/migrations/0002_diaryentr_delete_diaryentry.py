# Generated by Django 4.1.3 on 2022-11-18 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiaryEntr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(blank=True, default='', max_length=200)),
                ('date_cooked', models.DateField()),
                ('notes', models.TextField(blank=True)),
                ('recipe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.recipe')),
            ],
        ),
        migrations.DeleteModel(
            name='DiaryEntry',
        ),
    ]