# Generated by Django 4.1.3 on 2022-11-18 23:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_reactionentry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reactionentry',
            old_name='recipetype',
            new_name='reactiontype',
        ),
    ]