# Generated by Django 5.0.1 on 2024-01-02 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Genres',
            new_name='Genre',
        ),
    ]
