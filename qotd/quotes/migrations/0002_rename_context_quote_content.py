# Generated by Django 4.1.2 on 2022-10-25 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quote',
            old_name='context',
            new_name='content',
        ),
    ]
